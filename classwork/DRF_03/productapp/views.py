from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
# Create your views here.

class ProductView(APIView):
    def get(self,request):
        return Response("Get calling..")
    def post(self,request):
        return Response("Post Calling..")
    
class ProductRetriview(APIView):
    def put(self,request,id):
        return Response("Put calling..")
    def delete(self,request,id):
        return Response("Delete Calling..")
