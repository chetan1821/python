from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import APIView,api_view,permission_classes
from django.contrib.auth.models import User
from myapp.serializer import *
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def display(request):
    return Response({"msg":"display calling"})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def create(request):
    return Response({"msg":"view calling"})