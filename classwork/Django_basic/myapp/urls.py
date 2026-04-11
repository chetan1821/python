from django.urls import *
from myapp.views import *


urlpatterns = [
    path("",index,name="index"),
    path("about",about,name="about"),
    path("contact",contact,name="contact"),
]