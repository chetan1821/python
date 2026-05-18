from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import *
from myapp.serializer import *
# Create your views here.
class doctorapi(APIView):

    def post(self,request):
        serializer = DoctorSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"errors":serializer.error,"message":"somthing went wrong"})
        else:
            return Response({"data":serializer.data,"message":"Data inserted successfully"})

