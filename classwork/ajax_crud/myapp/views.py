from django.shortcuts import render
from myapp.models import *
from django.http import JsonResponse,HttpResponse
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,"index.html")

def display(request):
    students = Student.objects.all()
    return JsonResponse({"student":list(students.values())})

def add_user(request):
    if request.method == 'POST':
        data = request.POST
        name=data.get("name")
        email = data.get("email")
        age=data.get("age")
        course=data.get("course")

        Student.objects.create(name=name,email=email,age=age,course=course)
        return HttpResponse("Registration Successfullu !!!!")
    
def delete_user(request):
    id = request.GET['id']
    student=Student.objects.filter(id=id)
    student.delete()
    return HttpResponse("Student Delete...!!!")

def edit_user(request):
    id  = request.GET['id']
    student = Student.objects.filter(id=id)
    return JsonResponse({"student":list(student.values())})

def update_user(request):
    if request.method == 'POST':
        data = request.POST
        id = data.get("id")
        name=data.get("name")
        email = data.get("email")
        age=data.get("age")
        course=data.get("course")

        st=Student.objects.get(pk=id)
        st.name=name
        st.email=email
        st.age=age
        st.course=course
        st.save()

        return HttpResponse("Update Successfull")


def search(request):
    s = request.GET['s']
    students = Student.objects.filter(
        Q(name__startswith=s)|
        Q(email__startswith=s)|
        Q(age__startswith=s)|
        Q(course__startswith=s))
    return JsonResponse({"students": list(students.values())})