from rest_framework import serializers
from myapp.models import *

class Doctorser(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"