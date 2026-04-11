from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.
# def index(request):
#     products=Product.objects.all()
#     if request.method=='POST':
#         data=request.POST
#         name=data.get("name")
#         price=data.get("price")
#         category=data.get("category")
#         stock=data.get("stock")
#         image=request.FILES.get("file")

#         Product.objects.create(
#             name=name,
#             price=price,
#             category=category,
#             stock=stock,
#             image=image
#         )
#         return redirect(index)
#     return render(request,"index.html",{"products":products})



def index(request):
    products = Product.objects.all()

    # 👉 get edit id from URL
    eid = request.GET.get('eid')

    # 👉 POST (ADD + UPDATE)
    if request.method == 'POST':
        data = request.POST

        id = data.get("id")   # will be None for add
        name = data.get("name")
        price = data.get("price")
        category = data.get("category")
        stock = data.get("stock")
        image = request.FILES.get("file")

        # 👉 UPDATE (if id exists)
        if id:
            product = Product.objects.get(id=id)
            product.name = name
            product.price = price
            product.category = category
            product.stock = stock

            # only update image if new uploaded
            if image:
                products.image=image

            product.save()

        # 👉 ADD (else)
        else:
            Product.objects.create(
                name=name,
                price=price,
                category=category,
                stock=stock,
                image=image
            )

        return redirect('/')   # reload page

    return render(request, "index.html", {
        "products": products,
        "eid": int(eid) if eid else None
    })

# Update Data
# def update(request):
#     products=Product.objects.all()
#     uid = request.GET.get('uid')
#     if request.method=='POST':
#         data=request.POST
#         name=data.get("name")
#         price=data.get("price")
#         category=data.get("category")
#         stock=data.get("stock")
#         image = request.FILES.get("file")


#         products=Product.objects.get(pk=uid)
#         products.name=name
#         products.price=price
#         products.category=category
#         products.stock=stock
#         products.image=image
#         products.save()

#         return redirect(index)

#     uproducts=Product.objects.get(pk=uid)
#     return render(request,"index.html",{"uproducts":uproducts,"products":products})

# Delete Item
def delete(request):
    did=request.GET.get("did")
    dproduct=Product.objects.get(pk=did)
    dproduct.delete()
    return redirect(index)

