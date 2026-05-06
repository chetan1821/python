from rest_framework import viewsets, permissions
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import timedelta
from rest_framework.decorators import action
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from .permissions import IsAdminOrTeacher, IsAdminTeacherOrStudentReadOnly
from .models import Teacher, Course, Student, Attendance, Exam, Result, Notice, Installment
from .serializers import (
    TeacherSerializer, CourseSerializer, StudentSerializer, 
    AttendanceSerializer, ExamSerializer, ResultSerializer, 
    NoticeSerializer, InstallmentSerializer, MyTokenObtainPairSerializer, UserSerializer
)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    permission_classes = (permissions.AllowAny,)

class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'])
    def change_password(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        
        if not user.check_password(old_password):
            return Response({"error": "Incorrect current password"}, status=400)
            
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)
        return Response({"message": "Password updated successfully"})

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminTeacherOrStudentReadOnly]

    def perform_destroy(self, instance):
        user = instance.user
        if user:
            user.delete()
        else:
            instance.delete()

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminTeacherOrStudentReadOnly]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminTeacherOrStudentReadOnly]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or hasattr(user, 'teacher_profile'):
            queryset = Student.objects.all()
            teacher_id = self.request.query_params.get('teacher')
            if teacher_id:
                queryset = queryset.filter(course__teacher_id=teacher_id)
            return queryset
        
        if hasattr(user, 'student_profile'):
            return Student.objects.filter(id=user.student_profile.id)
            
        return Student.objects.none()

    def perform_destroy(self, instance):
        user = instance.user
        if user:
            user.delete()
        else:
            instance.delete()

class InstallmentViewSet(viewsets.ModelViewSet):
    queryset = Installment.objects.all()
    serializer_class = InstallmentSerializer
    permission_classes = [IsAdminTeacherOrStudentReadOnly]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or hasattr(user, 'teacher_profile'):
            queryset = Installment.objects.all()
            student_id = self.request.query_params.get('student')
            if student_id:
                queryset = queryset.filter(student_id=student_id)
            return queryset.order_by('-payment_date')
            
        if hasattr(user, 'student_profile'):
            return Installment.objects.filter(student=user.student_profile).order_by('-payment_date')
            
        return Installment.objects.none()

    def perform_create(self, serializer):
        student = serializer.validated_data['student']
        amount = serializer.validated_data['amount']
        
        remaining = float(student.total_fees) - float(student.fees_paid)
        if float(amount) > remaining + 0.01: # Small margin for float precision
            raise ValidationError(f"Amount exceeds remaining balance of ₹{remaining}")
            
        # Save the installment
        installment = serializer.save()
        
        # Update student balance and status
        student.fees_paid += installment.amount
        total = float(student.total_fees)
        paid = float(student.fees_paid)
        
        if paid >= total:
            student.fees_status = 'Paid'
        elif paid > 0:
            student.fees_status = 'Partial'
        student.save()

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAdminTeacherOrStudentReadOnly]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or hasattr(user, 'teacher_profile'):
            return Attendance.objects.all()
        if hasattr(user, 'student_profile'):
            return Attendance.objects.filter(student=user.student_profile)
        return Attendance.objects.none()

    @action(detail=False, methods=['post'], permission_classes=[IsAdminOrTeacher])
    def bulk_mark(self, request):
        date = request.data.get('date')
        attendance_data = request.data.get('attendance', []) # List of {student_id, status}
        
        if not date or not attendance_data:
            return Response({"error": "Date and attendance data are required"}, status=400)
            
        created_records = []
        for item in attendance_data:
            record, created = Attendance.objects.update_or_create(
                student_id=item['student_id'],
                date=date,
                defaults={'status': item['status']}
            )
            created_records.append(record.id)
            
        return Response({"message": f"Attendance marked for {len(created_records)} students", "ids": created_records})

    @action(detail=False, methods=['get'])
    def student_stats(self, request):
        user = self.request.user
        student_id = request.query_params.get('student_id')
        
        # If user is a student, they can ONLY see their own stats
        if hasattr(user, 'student_profile'):
            student_id = user.student_profile.id
        elif not student_id:
            return Response({"error": "student_id is required"}, status=400)
            
        qs = Attendance.objects.filter(student_id=student_id)
        total = qs.count()
        present = qs.filter(status='present').count()
        percentage = (present / total * 100) if total > 0 else 0
        
        return Response({
            "total": total,
            "present": present,
            "absent": total - present,
            "percentage": round(percentage, 1),
            "history": AttendanceSerializer(qs.order_by('-date')[:10], many=True).data
        })

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsAdminTeacherOrStudentReadOnly]

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [IsAdminTeacherOrStudentReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or hasattr(user, 'teacher_profile'):
            return Result.objects.all()
        if hasattr(user, 'student_profile'):
            return Result.objects.filter(student=user.student_profile)
        return Result.objects.none()

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [IsAdminTeacherOrStudentReadOnly]

class DashboardStatsViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        if not (request.user.is_staff or request.user.is_superuser or hasattr(request.user, 'teacher_profile')):
            return Response({"error": "Unauthorized"}, status=403)

        total_students = Student.objects.count()
        total_courses = Course.objects.count()
        total_teachers = Teacher.objects.count()
        
        fees_data = Student.objects.aggregate(
            total_collected=Sum('fees_paid'),
            total_expected=Sum('total_fees')
        )
        
        total_collected = fees_data['total_collected'] or 0
        total_expected = fees_data['total_expected'] or 0
        total_pending = total_expected - total_collected
        
        # Enrollment Growth (last 6 months)
        growth_data = []
        today = timezone.now()
        for i in range(5, -1, -1):
            # Calculate month and year for the past i months
            month_date = today - timedelta(days=i*30)
            month_name = month_date.strftime('%b')
            count = Student.objects.filter(joined_date__month=month_date.month, joined_date__year=month_date.year).count()
            growth_data.append({"name": month_name, "students": count})

        # Course stats
        course_stats = []
        for course in Course.objects.all():
            count = Student.objects.filter(course=course).count()
            # Calculate a pseudo-progress based on some criteria or just use a placeholder
            course_stats.append({
                "name": course.name,
                "students": f"{count}+" if count > 0 else "0",
                "progress": 70 if count > 0 else 0, # Placeholder
                "color": "bg-indigo-500"
            })

        return Response({
            "totalStudents": total_students,
            "totalCourses": total_courses,
            "totalTeachers": total_teachers,
            "feesCollected": float(total_collected),
            "pendingFees": float(total_pending),
            "studentGrowth": growth_data,
            "courseStats": course_stats[:3] # Return top 3
        })
