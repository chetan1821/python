from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
# Create your views here.
class StudentView(APIView):
    def get(self,request):
        return Response("GET Calling")
    def post(self,request):
        return Response("Post Calling")
    
class StudentUpdate(APIView):
    def put(self,request,id):
        return Response("put calling..")
    def delete(self,request,id):
        return Response("Delete calling..")

