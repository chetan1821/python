from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from myapp.models import *
from myapp.serializers import *
# Create your views here.

class DoctorAPIView(APIView):
     def get(self, request):
          
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)

        return Response(serializer.data)
     
     def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

     