from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Teacher, Course, Student, Attendance, Exam, Result, Notice, Installment

class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role', 'first_name')

    def get_role(self, obj):
        if obj.is_superuser or obj.is_staff:
            return 'admin'
        if hasattr(obj, 'teacher_profile'):
            return 'teacher'
        return 'student'

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializer(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

    def create(self, validated_data):
        email = validated_data.get('email')
        name = validated_data.get('name')
        
        if email:
            # Check if user already exists
            user = User.objects.filter(username=email).first()
            
            if user:
                # If user exists, check if they are already a teacher
                if hasattr(user, 'teacher_profile'):
                    raise serializers.ValidationError({"email": "A teacher with this email already exists."})
                # If they exist (maybe as student or admin), we link them
                user.first_name = name
                user.save()
            else:
                # Create new user
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    first_name=name,
                    password='password123'
                )
            
            validated_data['user'] = user
            
        return super().create(validated_data)

class CourseSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source='teacher.name', read_only=True)
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name', read_only=True)
    teacher_name = serializers.CharField(source='course.teacher.name', read_only=True)
    
    class Meta:
        model = Student
        fields = '__all__'

    def calculate_status(self, data):
        total = float(data.get('total_fees', 0))
        paid = float(data.get('fees_paid', 0))
        if paid >= total and total > 0:
            return 'Paid'
        elif paid > 0:
            return 'Partial'
        return 'Pending'

    def create(self, validated_data):
        course = validated_data.get('course')
        if course and not validated_data.get('total_fees'):
            validated_data['total_fees'] = course.fees
        
        validated_data['fees_status'] = self.calculate_status(validated_data)
        
        # Automatically create a User account
        email = validated_data.get('email')
        name = validated_data.get('name')
        user, _ = User.objects.get_or_create(username=email, email=email, defaults={'first_name': name})
        user.set_password('password123')
        user.save()
        validated_data['user'] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        total = validated_data.get('total_fees', instance.total_fees)
        paid = validated_data.get('fees_paid', instance.fees_paid)
        
        if total < 0:
            raise serializers.ValidationError({"total_fees": "Total fees cannot be negative."})
        if paid < 0:
            raise serializers.ValidationError({"fees_paid": "Fees paid cannot be negative."})
            
        # Only recalculate status if fees data is actually present or we're updating
        instance.fees_status = self.calculate_status({
            'total_fees': total,
            'fees_paid': paid
        })
        
        return super().update(instance, validated_data)

    def validate_total_fees(self, value):
        if value < 0:
            raise serializers.ValidationError("Total fees cannot be negative.")
        return value

    def validate_fees_paid(self, value):
        if value < 0:
            raise serializers.ValidationError("Fees paid cannot be negative.")
        return value

class InstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installment
        fields = '__all__'

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Installment amount must be greater than zero.")
        return value

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name', read_only=True)
    class Meta:
        model = Exam
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.name', read_only=True)
    exam_title = serializers.CharField(source='exam.title', read_only=True)
    class Meta:
        model = Result
        fields = '__all__'

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'
