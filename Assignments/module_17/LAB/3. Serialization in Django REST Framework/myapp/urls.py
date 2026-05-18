from django.urls import path
from myapp.views import *

urlpatterns = [
     path('doctor/', DoctorAPIView.as_view())
]
