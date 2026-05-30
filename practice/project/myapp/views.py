from django.shortcuts import render
from rest_framework.response import Response
from myapp.models import *
from myapp.serializer import *
from rest_framework import viewsets, status
# Create your views here.
def index(request):
    return  Response("done")


class CategoryViewset(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewset(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

