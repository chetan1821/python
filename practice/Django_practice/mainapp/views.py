from django.shortcuts import render
from .models import *
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,"contact.html")

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        password = request.POST.get('password')

        Student.objects.create(
            name=name,
            email=email,
            age=age,
            password=password
        )

        # return redirect('register')  # or success page

    return render(request, 'register.html')