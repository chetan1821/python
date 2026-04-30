from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myapp.models import *

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

