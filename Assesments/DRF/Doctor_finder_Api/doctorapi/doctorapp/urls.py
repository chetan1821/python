from django.urls import path
from doctorapp.views import *
urlpatterns = [
    path("doctors/",DoctorView.as_view()),
    path("doctors/<id>",DoctorViewRetrive.as_view())
]
