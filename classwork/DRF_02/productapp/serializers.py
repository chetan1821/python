from rest_framework import serializers
from productapp.models import *


class CategorySer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class ProductSer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

    def to_representation(self, instance):

        data = super().to_representation(instance)

        data['category'] = instance.category.name

        return data