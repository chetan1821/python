from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import Studentserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
# def studentView(request):
#     students= Student.objects.all()
#     # print(students)
#             # maually seralization
#             # st_list=list(students.values())
#             # return JsonResponse(st_list,safe=False)
    
#     return JsonResponse(students)
@api_view(['GET','POST'])
def studentView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = Studentserializer(students,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=Studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def put_student(request,id):
    student=Student.objects.get(id=id)
    ser = Studentserializer(student,request.data,partial=True)
    if not ser.is_valid():
        return Response({"errors":ser.errors,"message":"somthing went wrong"})
    else:
        ser.save()
        return Response({"data":ser.data,"meassage":"data updated.."})

@api_view(['DELETE'])
def delete_student(request,id):
    studet=Student.objects.get(id=id)
    studet.delete()
    return Response("delete")





