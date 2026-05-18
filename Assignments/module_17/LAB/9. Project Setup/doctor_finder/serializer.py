from rest_framework import serializers
from doctor_finder.models import *

class Doctorser(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"