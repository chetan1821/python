from django.shortcuts import render
from rest_framework.decorators import APIView
from django.contrib.auth.models import User
from myapp.serializer import *
from rest_framework.response import Response

class UserAPIView(APIView):

    def get(self,request):
        users = User.objects.all()
        ser = UserSerilaizer(users,many=True)
        return Response({"data":ser.data})
    

    def post(self,request):
        ser = UserSerilaizer(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response({"data":ser.data})
        else:
            return Response({"errors":ser.errors})