from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from studentapp.models import *
from studentapp.serializer import *
# Create your views here.

@api_view(['GET'])
def get_student(request):
    students = Student.objects.all()
    ser =  StudentSerializer(students,many=True)
    return Response({"data":ser.data})

@api_view(['POST'])
def post_student(request):
    ser = StudentSerializer(data = request.data)
    if not ser.is_valid():
        return Response({"errors":ser.errors,"message":"Something went wrong"})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"Data inserted succssfully !!!"})
    
@api_view(['PUT'])
def put_student(request,id):
    student = Student.objects.get(id=id)
    ser = StudentSerializer(student,request.data,partial=True)
    if not ser.is_valid():
        return Response({"errors":ser.errors,"message":"Something went wrong"})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"Data updated succssfully !!!"})

@api_view(['DELETE'])
def delete_student(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return Response({"message":"Student deleted"})
