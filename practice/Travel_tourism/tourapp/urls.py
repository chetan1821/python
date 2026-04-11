from django.urls import path
from tourapp.views import *
urlpatterns = [
    path('',index,name="index"),
]
