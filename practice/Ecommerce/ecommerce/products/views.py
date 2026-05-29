from rest_framework.response import Response
from rest_framework.views import APIView


class CategoryView(APIView):
    def get(self, request):
        return Response({"message": "Category API"})


class ProductView(APIView):
    def get(self, request):
        return Response({"message": "Product API"})

