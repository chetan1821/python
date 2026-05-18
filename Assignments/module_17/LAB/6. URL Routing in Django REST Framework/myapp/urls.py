from django.urls import path
from .views import *

urlpatterns = [

    path('doctors', DoctorAPIView.as_view()),

    path('doctors/<int:id>', DoctorAPIView.as_view()),
]