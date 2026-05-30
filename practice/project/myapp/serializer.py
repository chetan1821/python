from rest_framework import serializers
from django.contrib.auth.models import User

from .models import (
    Category,
    Product,
    Address,
    Cart,
    Order,
    OrderItem
)


# =========================
# User Serializer
# =========================
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        ]

        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password')
        )
        return user


# =========================
# Category Serializer
# =========================
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


# =========================
# Product Serializer
# =========================
class ProductSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(
        source='category.name',
        read_only=True
    )

    class Meta:
        model = Product
        fields = '__all__'


# =========================
# Address Serializer
# =========================
class AddressSerializer(serializers.ModelSerializer):

    user_name = serializers.CharField(
        source='user.username',
        read_only=True
    )

    class Meta:
        model = Address
        fields = '__all__'


# =========================
# Cart Serializer
# =========================
class CartSerializer(serializers.ModelSerializer):

    user_name = serializers.CharField(
        source='user.username',
        read_only=True
    )

    product_name = serializers.CharField(
        source='product.name',
        read_only=True
    )

    class Meta:
        model = Cart
        fields = '__all__'


# =========================
# Order Item Serializer
# =========================
class OrderItemSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(
        source='product.name',
        read_only=True
    )

    class Meta:
        model = OrderItem
        fields = '__all__'


# =========================
# Order Serializer
# =========================
class OrderSerializer(serializers.ModelSerializer):

    user_name = serializers.CharField(
        source='user.username',
        read_only=True
    )

    order_items = OrderItemSerializer(
        source='orderitem_set',
        many=True,
        read_only=True
    )

    class Meta:
        model = Order
        fields = '__all__'