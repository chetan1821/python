from django.urls import path
from student_app.views import *
urlpatterns = [
    path("",index,name="index"),
]
