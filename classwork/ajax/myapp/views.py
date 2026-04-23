from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *

# Create your views here.
def index(request):
    return render(request,"index.html")
# def test(request):
#     uname=request.GET['uname']
#     return HttpResponse(f"Hello {uname}")
def search(request):
    q=request.GET['q']
    pro="<ul>"
    products = Product.objects.filter(name__startswith=q)
    for i in products:
        pro+=f"<li>{i.name}</li>"
    
    pro+="</ul>"
    return HttpResponse(pro)





