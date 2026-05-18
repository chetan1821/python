from rest_framework import serializers
from myapp.models import *

class Doctorseralizer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"