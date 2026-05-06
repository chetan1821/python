from django.shortcuts import render
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from productapp.models import *
from productapp.serializers import *
# Create your views here.
class ProductView(APIView):
    def get(self,request):
        products = Product.objects.all()
        ser = ProductSer(products, many=True)
        return Response({"data": ser.data})
    def post(self,request):
        ser =ProductSer(data = request.data,many=True)
        if ser.is_valid():
            ser.save()
            return Response({"data":ser.data})
        else:
            return Response({"error":ser.errors})
class ProductRetrive(APIView):
    def put(self,request,id):
        product=Product.objects.get(pk=id)
        ser =ProductSer(product,data = request.data)
        if ser.is_valid():
            ser.save()
            return Response({"data":ser.data})
        else:
            return Response({"error":ser.errors})

    def delete(self,request,id):
        product =Product.objects.get(pk=id)
        product.delete()
        return Response("Done")
    
class CategoryView(APIView):
    def get(self,request):
        categories=Category.objects.all()
        ser = CategorySer(categories,many=True)
        return Response({"data":ser.data})
    def post(self,request):
        ser =CategorySer(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response({"data":ser.data})
        else:
            return Response({"error":ser.errors})
        
class CategoryRetrive(APIView):
    def put(self,request,id):
        category = Category.objects.get(pk=id)
        ser =CategorySer(category,data = request.data)
        if ser.is_valid():
            ser.save()
            return Response({"data":ser.data})
        else:
            return Response({"error":ser.errors})
        
    def delete(self,request,id):
        category = Category.objects.get(pk=id)
        category.delete()
        return Response("Done")
    
@api_view(['GET'])
def product_by_category(request,id):
    category=Category.objects.get(pk=id)
    product=Product.objects.filter(category=category)
    ser = ProductSer(product,many=True)
    return Response({"data":ser.data})
