from django.shortcuts import render
from myapp.models import *
from django.core.paginator import Paginator
# Create your views here.
from django.db.models import Sum


def index(request):
    student = Student.objects.all()
    paginator = Paginator(student, 5)  

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    
    return render(request,"index.html",{"students":page_obj})

def report(request):
    sid = request.GET['sid']
    student = Student.objects.get(id=sid)
    marks = Marks.objects.filter(student=student)
    total = marks.aggregate(total_marks=Sum("Marks"))
    
    students = Student.objects.annotate(total_marks=Sum('marks__Marks')).order_by("-total_marks")
    
    r = 1
    rank = 0
    for i in students:
        if int(i.id)==int(sid):
            rank=r
        r+=1
    

    return render(request,"report.html",{"marks":marks,"sum":total['total_marks'],"rank":rank})


