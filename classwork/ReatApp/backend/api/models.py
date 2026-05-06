from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile', null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)
    subject = models.CharField(max_length=100)
    courses_count = models.IntegerField(default=0)
    joined_date = models.DateField()
    
    # Preferences
    email_notifications = models.BooleanField(default=True)
    exam_alerts = models.BooleanField(default=True)
    attendance_reports = models.BooleanField(default=True)
    announcement_notifications = models.BooleanField(default=True)
    accent_color = models.CharField(max_length=20, default='#4f46e5')

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    duration = models.CharField(max_length=50)
    fees = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile', null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    total_fees = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fees_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fees_status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Partial', 'Partial'), ('Pending', 'Pending')], default='Pending')
    joined_date = models.DateField()

    # Preferences
    email_notifications = models.BooleanField(default=True)
    exam_alerts = models.BooleanField(default=True)
    attendance_reports = models.BooleanField(default=True)
    announcement_notifications = models.BooleanField(default=True)
    accent_color = models.CharField(max_length=20, default='#4f46e5')

    def __str__(self):
        return self.name

class Installment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='installments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    remarks = models.CharField(max_length=200, null=True, blank=True)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])

class Exam(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    duration = models.CharField(max_length=50)
    total_marks = models.IntegerField()
    date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Upcoming', 'Upcoming'), ('Active', 'Active'), ('Completed', 'Completed')])

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks = models.IntegerField()
    total = models.IntegerField()
    grade = models.CharField(max_length=5)

class Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    priority = models.CharField(max_length=10, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')])
