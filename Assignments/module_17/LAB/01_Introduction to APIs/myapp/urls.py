from django.urls import path
from .views import *

urlpatterns = [

    path('joke/', joke_api),

]