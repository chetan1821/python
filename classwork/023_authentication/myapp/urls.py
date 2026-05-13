from django.urls import path
from myapp.views import *

urlpatterns = [
    path("users",UserAPIView.as_view())
]