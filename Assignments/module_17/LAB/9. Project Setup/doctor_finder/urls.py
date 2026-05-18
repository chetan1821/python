from django.urls import path
from doctor_finder.views import *

urlpatterns = [
    path("doctor/",Doctordata.as_view())
]
