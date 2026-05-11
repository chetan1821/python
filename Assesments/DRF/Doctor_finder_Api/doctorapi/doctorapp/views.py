from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from doctorapp.serializers import *
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.
class DoctorView(APIView):
    def get(self,request):
        doctors = Doctor.objects.all()
        ser = doctorSer(doctors,many=True)
        return Response({"data":ser.data},status=status.HTTP_200_OK)

    def post(self,request):
        ser = doctorSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"data":ser.data,"message":"Data inserted Successfully.."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"data":ser.data,"message":"somthings went wrong.."}, status=status.HTTP_400_BAD_REQUEST)
class DoctorViewRetrive(APIView):
    def get(self, request, id):

        doctor = get_object_or_404(Doctor, pk=id)

        ser = doctorSer(doctor)

        return Response(
            {"data": ser.data},
            status=status.HTTP_200_OK
        )

    def put(self,request,id):
        doctor = get_object_or_404(Doctor, pk=id)
        ser = doctorSer(doctor,data=request.data)
        if ser.is_valid():
                ser.save()
                return Response({"data":ser.data,"message":"Data Updated Successfully.."},status=status.HTTP_200_OK)
        else:
            return Response({"errors": ser.errors},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        doctor = get_object_or_404(Doctor, pk=id)
        doctor.delete()
        return Response({"message":"Data Deleted..!"})
