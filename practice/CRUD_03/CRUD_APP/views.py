from django.shortcuts import render,redirect
from CRUD_APP.models import *
# Create your views here.
def index(request):
    peoples=People.objects.all()
    if request.method == 'POST':
        data=request.POST

        name=data.get("name")
        age=data.get("age")
        phone=data.get("phone")
        image=request.FILES.get("file")

        People.objects.create(
            name=name,
            age=age,
            phone=phone,
            image=image
        )
        return redirect(index)
    return render(request,"index.html",{"peoples":peoples})


def delete(request):
    did=request.GET.get('did')
    pe=People.objects.get(pk=did)
    pe.delete()
    return redirect(index)

def update(request):
    peoples=People.objects.all()
    uid=request.GET.get('uid')
    if request.method == 'POST':
        data=request.POST

        name=data.get("name")
        age=data.get("age")
        phone=data.get("phone")

        peoples=People.objects.get(pk=uid)
        peoples.name=name
        peoples.age=age
        peoples.phone=phone
        peoples.save()


        return redirect(index)
    upeoples=People.objects.get(pk=uid)
    return render(request,"index.html",{"upeople":upeoples,"peoples":peoples})

