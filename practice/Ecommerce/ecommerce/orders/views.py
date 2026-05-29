from rest_framework.views import APIView
from rest_framework.response import Response


class CartView(APIView):
    def get(self, request):
        return Response({"message": "Cart API"})


class WishlistView(APIView):
    def get(self, request):
        return Response({"message": "Wishlist API"})
    
class OrderView(APIView):

    def get(self, request):
        return Response({"message": "Order API"})


class OrderItemView(APIView):

    def get(self, request):
        return Response({"message": "Order Item API"})
