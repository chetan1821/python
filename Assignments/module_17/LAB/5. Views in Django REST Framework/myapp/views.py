from django.shortcuts import render
from myapp.models import *
from myapp.seralizer import *
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class doctordata(APIView):
    def get(self,request):
        doctors = Doctor.objects.all()
        ser = Doctorseralizer(doctors,many=True)
        return Response({"data":ser.data})
    
    def post(self,request):
        ser = Doctorseralizer(data=self.request.data)
        if not ser.is_valid():
            return Response({"errors":ser.error,"message":"Somating went Wrong"})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"data inserted successfully"})
        

class docotrviewRetrive(APIView):
    def put(self,request,id):
        doctors = Doctor.objects.get(id=id)
        ser = Doctorseralizer(doctors,request.data,partial=True)
        if not ser.is_valid():
            return Response({"errors":ser.errors,"message":"Something went Wrnog"})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"doctor data update successfully"})
        
    def delete(self,request,id):
        doctors = Doctor.objects.get(id=id)
        doctors.delete()
        return Response({"message":"doctor data is successfully delete"})
