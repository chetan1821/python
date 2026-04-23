from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import *

# Create your views here.
def index(request):
    return render(request,"index.html")
def test(request):
    uname=request.GET['uname']
    return HttpResponse(f"hello {uname}")

def search(request):
    p=request.GET.get('p')
    pro="<ul>"
    product= Product.objects.filter(name__startswith=p)
    for i in product:
        pro+=f"<li>{i.name}</li>"

    pro+="</ul>"
    return HttpResponse(pro)

def countries(request):
    all_countries= Country.objects.all()
    return JsonResponse({"data":list(all_countries.values())})

def state(request):
    cid = request.GET['cid']
    country =Country.objects.get(pk=cid)
    all_state=State.objects.filter(country=country)
    return JsonResponse({"data":list(all_state.values())})

def city(request):
    ccid = request.GET['ccid']
    state =State.objects.get(pk=ccid)
    all_city=City.objects.filter(state=state)
    return JsonResponse({"data":list(all_city.values())})

