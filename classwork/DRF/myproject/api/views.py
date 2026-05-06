from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_api(request):
    return Response("GET API CALLING")


@api_view(['POST'])
def post_api(request):
    return Response("POST API CALLING")


@api_view(['PUT'])
def put_api(request):
    return Response("PUT API CALLING")


@api_view(['DELETE'])
def delete_api(request):
    return Response("DELETE API CALLING")