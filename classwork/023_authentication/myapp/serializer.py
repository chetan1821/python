from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'

     


    # def create(self, validated_data):
    #     return User.objects.create_user(validated_data)
    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )

        return user
