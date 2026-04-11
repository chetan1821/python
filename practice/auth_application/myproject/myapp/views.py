from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        data = request.POST
        f_name = data.get('fname')
        l_name = data.get('lname')
        u_name = data.get('u_name')
        password = data.get('pwd')

        if User.objects.filter(username=u_name).exists():
            return render(request, "register.html", {'err': "Username already exists!"})

        u = User(first_name=f_name, last_name=l_name, username=u_name)
        u.set_password(password)
        u.save()

        return render(request, 'register.html', {"msg": "Registration successful.."})

    return render(request, 'register.html')

def login_page(request):
    if request.method=='POST':
        data=request.POST
        uname=data.get('u_name')
        pwd=data.get('pwd')

        u=authenticate(username=uname,password=pwd)
        if u is None:
            return render(request, "login.html",{"err":"Invalid Username Or Password"})
        else:
            login(request,u)
            return redirect('dashboard')


    return render(request, "login.html")

@login_required(login_url='login_page')
def dashboard(request):
    data = User.objects.all()
    return render(request, "dashboard.html",{"all_data": data})

def logout_user(request):
    logout(request)
    return redirect('login_page')