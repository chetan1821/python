from django.shortcuts import render,redirect
from EmpApp.models import *
# Create your views here.
def index(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        age = data.get("age")

        Employee.objects.create(
            name=name,
            email=email,
            age=age
        )
        return render(request,"index.html",{"msg":"registration suceess","employee":employees})
    return render(request,"index.html",{"employee":employees})

def delete(request):
    did =request.GET['did']
    emp = Employee.objects.get(id=did)
    emp.delete()
    return redirect('index')

def update(request):

    uid = request.GET.get("uid")

    emp = Employee.objects.get(id=uid)

    if request.method == 'POST':

        emp.name = request.POST.get("name")
        emp.email = request.POST.get("email")
        emp.age = request.POST.get("age")

        emp.save()

        return redirect('/')

    employees = Employee.objects.all()

    return render(request, "index.html", {
        "edit_emp": emp,
        "employee": employees
    })


    


from django.core.mail import send_mail
from django.http import HttpResponse

def send_email(request):

    subject = "Welcome to Django"
    
    message = "Hello Chetan, This email is sent using Django."

    from_email = None

    recipient_list = ['chetanpatil1821@gmail.com']

    send_mail(
        subject,
        message,
        from_email,
        recipient_list
    )

    return HttpResponse("Email Sent Successfully")


import random

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Send OTP
def send_otp(request):

    if request.method == "POST":

        email = request.POST.get('email')

        # Generate 4-digit OTP
        otp = random.randint(1000, 9999)

        # Store in session
        request.session['otp'] = str(otp)
        request.session['email'] = email

        # Send Email
        send_mail(
            'Your OTP Code',
            f'Your OTP is {otp}',
            'your_email@gmail.com',
            [email],
            fail_silently=False,
        )

        return redirect('verify_otp')

    return render(request, 'send_otp.html')


# Verify OTP
def verify_otp(request):

    if request.method == "POST":

        user_otp = request.POST.get('otp')

        saved_otp = request.session.get('otp')

        if user_otp == saved_otp:

            return HttpResponse("OTP Verified Successfully")

        else:

            return HttpResponse("Invalid OTP")

    return render(request, 'verify_otp.html')