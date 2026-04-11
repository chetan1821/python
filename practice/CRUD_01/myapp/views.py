from django.shortcuts import render,redirect
from myapp.models import *
import os
# Create your views here.
def index(request):
    employee=Employee.objects.all()
    if request.method=='POST':
        data=request.POST
        name=data.get("name")
        email=data.get("email")
        phone=data.get("phone")
        dept=data.get("dept")
        image = request.FILES.get("file")
        image2 = request.FILES.get("file2")

        Employee.objects.create(
            name=name,
            email=email,
            phone=phone,
            dept=dept,
            image=image,
            image2=image2
        )
        return redirect(index)

    return render(request,"index.html",{"employee":employee})

def delete(request):
    did=request.GET.get("did")
    employee=Employee.objects.get(pk=did)
    if employee.image and os.path.exists(employee.image.path):
        os.remove(employee.image.path)

    if employee.image2 and os.path.exists(employee.image2.path):
        os.remove(employee.image2.path)
    employee.delete()
    return redirect(index)

def update(request):
    employee=Employee.objects.all()
    if request.method=='POST':
        data=request.POST
        id=data.get("id")
        name=data.get("name")
        email=data.get("email")
        phone=data.get("phone")
        dept=data.get("dept")
        image = request.FILES.get("file")
        image2 = request.FILES.get("file2")


        employee=Employee.objects.get(pk=id)
        employee.name=name
        employee.email=email
        employee.phone=phone
        employee.dept=dept
        if request.FILES.get("file"):
            if employee.image and os.path.exists(employee.image.path):
                os.remove(employee.image.path)
            employee.image = request.FILES.get("file")

        if request.FILES.get("file2"):
            if employee.image2 and os.path.exists(employee.image2.path):
                os.remove(employee.image2.path)
            employee.image2 = request.FILES.get("file2")
        employee.save()

        return redirect("index")

    
    uid=request.GET['uid']
    employees=Employee.objects.get(pk=uid)

    return render(request,"index.html",{"employees":employees,"employee":employee})


