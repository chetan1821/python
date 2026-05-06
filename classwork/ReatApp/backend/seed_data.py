import os
import django
import random
from datetime import date, timedelta

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Teacher, Course, Student, User
from django.utils import timezone

def seed_data():
    print("Seeding data...")
    
    # 1. Create a Teacher if none exists
    teacher, created = Teacher.objects.get_or_create(
        email='teacher@example.com',
        defaults={
            'name': 'Prof. John Doe',
            'subject': 'Computer Science',
            'joined_date': date(2025, 1, 1)
        }
    )
    if created:
        print(f"Created teacher: {teacher.name}")
        # Create user for teacher
        user, _ = User.objects.get_or_create(username=teacher.email, email=teacher.email)
        user.set_password('password123')
        user.save()
        teacher.user = user
        teacher.save()

    # 2. Create Courses if none exist
    courses_data = [
        {'name': 'React Mastery', 'duration': '3 Months', 'fees': 5000},
        {'name': 'Python Bootcamp', 'duration': '2 Months', 'fees': 3500},
        {'name': 'UI/UX Design', 'duration': '4 Months', 'fees': 6000},
    ]
    
    created_courses = []
    for c_data in courses_data:
        course, created = Course.objects.get_or_create(
            name=c_data['name'],
            defaults={
                'teacher': teacher,
                'duration': c_data['duration'],
                'fees': c_data['fees']
            }
        )
        created_courses.append(course)
        if created:
            print(f"Created course: {course.name}")

    # 3. Create 10 Students
    names = [
        "Alice Smith", "Bob Johnson", "Charlie Brown", "David Wilson", 
        "Eva Garcia", "Frank Miller", "Grace Davis", "Henry Taylor", 
        "Ivy Martinez", "Jack Robinson"
    ]
    
    for i, name in enumerate(names):
        email = f"student{i+1}@example.com"
        # Check if student exists
        if Student.objects.filter(email=email).exists():
            print(f"Student {email} already exists, skipping.")
            continue
            
        course = random.choice(created_courses)
        total_fees = float(course.fees)
        fees_paid = random.choice([0, total_fees * 0.5, total_fees])
        
        # Joined date within last 5 months
        joined_date = date.today() - timedelta(days=random.randint(0, 150))
        
        student = Student.objects.create(
            name=name,
            email=email,
            mobile=f"98765432{i:02d}",
            address=f"Street {i+1}, Tech City",
            course=course,
            total_fees=total_fees,
            fees_paid=fees_paid,
            fees_status='Paid' if fees_paid >= total_fees else ('Partial' if fees_paid > 0 else 'Pending'),
            joined_date=joined_date
        )
        
        # Create User for student
        user, _ = User.objects.get_or_create(username=email, email=email, defaults={'first_name': name})
        user.set_password('password123')
        user.save()
        student.user = user
        student.save()
        
        print(f"Created student: {student.name} ({student.email})")

    print("Seeding complete!")

if __name__ == "__main__":
    seed_data()
