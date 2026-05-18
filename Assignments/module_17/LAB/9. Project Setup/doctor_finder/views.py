from django.shortcuts import render
from doctor_finder.models import *
from doctor_finder.serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class Doctordata(APIView):
    def get(self,request):
        doctor = Doctor.objects.all()
        ser = Doctorser(doctor,many = True)
        return Response({"data":ser.data})
    
    def post(self,request):
        ser = Doctorser(data=self.request.data)
        if not ser.is_valid():
            return Response({"errors":ser.errors,"message":"Somthing went Wrong"})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"data inserted successfully"})