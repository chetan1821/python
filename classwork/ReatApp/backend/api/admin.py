from django.contrib import admin
from .models import Teacher, Course, Student, Attendance, Exam, Result, Notice

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'courses_count')
    search_fields = ('name', 'subject')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'duration', 'fees')
    list_filter = ('teacher', 'duration')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'course', 'fees_status', 'joined_date')
    list_filter = ('course', 'fees_status')
    search_fields = ('name', 'email')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status')
    list_filter = ('date', 'status')

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'date', 'status')
    list_filter = ('status', 'course')

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'marks', 'total', 'grade')
    list_filter = ('exam', 'grade')

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'priority')
    list_filter = ('priority',)
