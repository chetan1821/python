from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# 🔹 Register (Student)
def index(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            course=request.POST.get("course"),
            password=request.POST.get("password")
        )
        return redirect('login')   # ✅ important

    return render(request, "index.html")


# 🔹 Login
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Student.objects.filter(email=email, password=password).first()

        if user:
            request.session['user_id'] = user.id
            return redirect('product_list')   # ✅ better

        else:
            return render(request, 'login.html', {
                'error': 'Invalid Email or Password'
            })

    return render(request, 'login.html')


# 🔹 Logout
def logout_view(request):
    request.session.flush()
    return redirect('login')


# 🔹 Employee Page
def employee(request):
    return render(request, "employee.html")


# 🔹 Add Product (Protected 🔒)
def product(request):
    if 'user_id' not in request.session:
        return redirect('login')

    if request.method == "POST":
        Product.objects.create(
            name=request.POST.get('name'),
            category=request.POST.get('category'),
            price=request.POST.get('price'),
            quantity=request.POST.get('quantity'),
            description=request.POST.get('description'),
            image=request.FILES.get('image')
        )
        return redirect('product_list')   # ✅ redirect after add

    return render(request, "product.html")


# 🔹 Product List (Protected 🔒)
def product_list(request):
    if 'user_id' not in request.session:
        return redirect('login')

    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


# 🔹 Delete Product (Safe)
def delete_product(request, id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=id)
        product.delete()

    return redirect('product_list')