from django.urls import path
from myapp.views import *

urlpatterns = [
    path("doctor/",doctorapi.as_view())
]
