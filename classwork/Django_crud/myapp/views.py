from django.shortcuts import render, redirect,get_object_or_404
from myapp.models import *
# Create your views here.
# Admin panel username=chetan pwd=1821

def student(request):
    if request.method == 'POST':
        data = request.POST

        name = data.get("name")
        email = data.get("email")
        age = data.get("age")
        course = data.get("course")

        Student.objects.create(
            name=name,
            email=email,
            age=age,
            course=course
        )

        return redirect('student')   

    all_data = Student.objects.all()
    return render(request, "student.html", {"studentss": all_data})

def delete(request):
    did=request.GET['did']
    st=Student.objects.get(id=did)
    st.delete()
    return redirect('student')






def employee(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        salary=data.get("salary")
        designation = data.get("designation")
        department = data.get("department")

        Employee.objects.create(
            name=name,
            email=email,
            salary=salary,
            designation =designation,
            department=department
            )
        return redirect('employee')
    
    all_data=Employee.objects.all()

    return render(request,"employee.html",{"emp":all_data})

def del_emp(request):
    dle=request.GET['dle']
    em=Employee.objects.get(id=dle)
    em.delete()
    return redirect("employee")


def product(request):
    if request.method == 'POST':
        data=request.POST

        product_name=data.get("product_name")
        price=data.get("price")
        quantity=data.get("quantity")
        description=data.get("description")

        Product.objects.create(
            product_name=product_name,
            price = price,
            quantity = quantity,
            description = description
        )
        return redirect("product")
    all_data=Product.objects.all()
        

    return render(request,"product.html",{"products":all_data})

def del_product(request):
    dle=request.GET['dle']
    pd=Product.objects.get(id=dle)
    pd.delete()
    return redirect("product")