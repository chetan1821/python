from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def get_api(request):
     return Response({"message": "GET API CALLING"})

@api_view(['POST'])
def post_api(request):
     return Response({"message":"POST API CAllinng"})

@api_view(['PUT'])
def put_api(request):
     return Response({"message":"PUT API CAllinng"})

@api_view(['DELETE'])
def del_api(request):
     return Response({"message":"Delete API CAllinng"})
