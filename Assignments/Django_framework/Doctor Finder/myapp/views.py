from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myapp.models import *
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Doctor

# Create your views here.

def login_page(request):
    if request.method=='POST':
        data = request.POST
        uname = data.get('uname')
        pwd = data.get('pwd')

        u = authenticate(username=uname,password=pwd)
        if u is None:
            return render(request,"login.html",{"err":"Invalid crednetials"})
        else:
            login(request,u)
            return redirect("index")


    if request.user.is_authenticated:
         return render(request,"index.html")
    return render(request,"login.html")
def reg(request):
    if request.method=='POST':
        data = request.POST
        fname = data.get('fname')
        lname = data.get('lname')
        uname = data.get('uname')
        pwd = data.get('password')

        if User.objects.filter(username=uname).exists():
            return render(request,"reg.html",{"err":"Username exist !!! "})

        u = User(first_name=fname,last_name=lname,username=uname)
        u.set_password(pwd)
        u.save()

        return render(request,"reg.html",{"msg":"Registration successful"})
    return render(request,"reg.html")

@login_required(login_url='login')
def index(request):
    doctor = Doctor.objects.all()
    return render(request,"index.html",{"doctors":doctor})


def user_logout(request):
    logout(request)
    return redirect("login")

def doctor_info(request):
    doctor = Doctor.objects.all()
    return render(request,"doctor.html",{"doctors":doctor})

# PAGE VIEW
def profile(request):

    doctors = Doctor.objects.all()

    return render(request, "profile.html", {
        "doctors": doctors
    })


# CREATE
def add_doctor(request):

    if request.method == "POST":

        doctor = Doctor.objects.create(

            name=request.POST.get('name'),
            specialization=request.POST.get('specialization'),
            experience=request.POST.get('experience'),
            fees=request.POST.get('fees'),
            rating=request.POST.get('rating'),
            location=request.POST.get('location'),
            image=request.FILES.get('image')

        )

        data = {
            "id": doctor.id,
            "name": doctor.name,
            "specialization": doctor.specialization,
            "experience": doctor.experience,
            "fees": doctor.fees,
            "rating": doctor.rating,
            "location": doctor.location,
            "image": doctor.image.url if doctor.image else ""
        }

        return JsonResponse({
            "status": "success",
            "doctor": data
        })


# UPDATE
def update_doctor(request, id):

    doctor = get_object_or_404(Doctor, pk=id)

    if request.method == "POST":

        doctor.name = request.POST.get('name')
        doctor.specialization = request.POST.get('specialization')
        doctor.experience = request.POST.get('experience')
        doctor.fees = request.POST.get('fees')
        doctor.rating = request.POST.get('rating')
        doctor.location = request.POST.get('location')

        if request.FILES.get('image'):
            doctor.image = request.FILES.get('image')

        doctor.save()

        return JsonResponse({
            "status": "updated"
        })


# DELETE
def delete_doctor(request, id):

    doctor = get_object_or_404(Doctor, pk=id)

    doctor.delete()

    return JsonResponse({
        "status": "deleted"
    })


def contact(request):
    if request.method=='POST':
        data=request.POST
        name=data.get('name')
        email=data.get('email')
        subject=data.get('subject')
        msg=data.get('msg')

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            msg=msg
        )
    return render(request,"contact.html")