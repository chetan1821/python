import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User
from api.models import Teacher, Course, Student, Notice, Exam
from datetime import date

def setup_app():
    # 1. Create Users
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@enjoy.com', 'password123')
        print("Superuser 'admin' created.")
    else:
        print("Superuser 'admin' already exists.")

    if not User.objects.filter(username='student').exists():
        student_user = User.objects.create_user('student', 'student@enjoy.com', 'password123')
        print("User 'student' created.")
    else:
        student_user = User.objects.get(username='student')
        print("User 'student' already exists.")

    # Link student user to a profile if not linked
    if not Student.objects.filter(user=student_user).exists():
        course = Course.objects.first()
        Student.objects.create(
            user=student_user,
            name='Student User',
            email='student@enjoy.com',
            course=course,
            fees_status='Paid',
            joined_date=date(2026, 1, 1)
        )
        print("Linked 'student' user to a Student profile.")

    # 2. Seed Data if empty
    if Teacher.objects.count() == 0:
        t1 = Teacher.objects.create(name='Dr. Sarah Connor', subject='Computer Science', courses_count=4, joined_date=date(2025, 11, 1))
        t2 = Teacher.objects.create(name='Prof. Xavier', subject='Psychology', courses_count=2, joined_date=date(2025, 12, 15))
        
        c1 = Course.objects.create(name='React Mastery', teacher=t1, duration='3 Months', fees=15000)
        c2 = Course.objects.create(name='UI/UX Design', teacher=t2, duration='2 Months', fees=10000)
        
        Student.objects.create(name='Alice Johnson', email='alice@enjoy.com', course=c1, fees_status='Paid', joined_date=date(2026, 1, 15))
        Student.objects.create(name='Bob Smith', email='bob@enjoy.com', course=c2, fees_status='Pending', joined_date=date(2026, 2, 10))
        
        Notice.objects.create(title='Summer Vacations', content='The institute will be closed from June 1st to June 15th.', priority='High')
        
        Exam.objects.create(title='React Basics Quiz', course=c1, duration='30 mins', total_marks=50, date=date(2026, 5, 10), status='Upcoming')
        print("Database seeded with sample data.")
    else:
        print("Database already has data.")

if __name__ == '__main__':
    setup_app()
