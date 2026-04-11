from django.shortcuts import render,redirect
from myapp.models import *
import os
# Create your views here.
def index(request):
    category=Category.objects.all()
    products=Product.objects.all()
    return render(request,"index.html",{"category":category,"product":products})

def add_product(request):
    if request.method=='POST':
        data= request.POST
        category=data.get('category')
        name=data.get('name')
        price=data.get('price')
        qty=data.get('qty')
        image=request.FILES.get('image')

        catobj=Category.objects.get(id=category)
        Product.objects.create(
            category=catobj,
            name=name,
            price=price,
            qty=qty,
            image=image
        )

    return redirect("index")

def delete(request):
    did = request.GET.get("did")
    p = Product.objects.get(pk=did)
    os.remove(p.image.path)
    p.delete()
    return redirect("index")

# def update(request):
#     if request.method=='POST':
#         id = data.get("id")
#         data= request.POST
#         category=data.get('category')
#         name=data.get('name')
#         price=data.get('price')
#         qty=data.get('qty')
#         image=request.FILES.get('image')

#         uproduct = Product.objects.get(pk=id)
#         catobj = Category.objects.get(id=category)
#         uproduct.category = catobj
#         uproduct.name=name
#         uproduct.price=price
#         uproduct.qty=qty

#         if request.FILES.get("image"):
#             if uproduct.image:
#                 os.remove(uproduct.image.path)

#             uproduct.image = request.FILES.get("image")

#         uproduct.save()

#         return redirect("index")
#     products=Product.objects.all()
#     uid=request.GET['uid']
#     uproduct=Product.objects.get(pk=uid)

#     return render(request,"index.html",{"category": category,
#         "product": products,
#         "edit": uproduct})

def update(request):
    category = Category.objects.all()  

    if request.method == 'POST':
        data = request.POST

        id = data.get("id")
        name = data.get('name')
        price = data.get('price')
        qty = data.get('qty')
        category_id = data.get('category')

        uproduct = Product.objects.get(pk=id)
        catobj = Category.objects.get(id=category_id)

        uproduct.category = catobj
        uproduct.name = name
        uproduct.price = price
        uproduct.qty = qty

        if request.FILES.get("image"):
            if uproduct.image:
                os.remove(uproduct.image.path)
            uproduct.image = request.FILES.get("image")

        uproduct.save()
        return redirect("index")

    uid = request.GET.get("uid")
    uproduct = Product.objects.get(pk=uid)
    products = Product.objects.all()

    return render(request, "index.html", {
        "category": category,
        "product": products,
        "edit": uproduct
    })





