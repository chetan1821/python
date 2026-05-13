from django.urls import path
from myapp.views import *

urlpatterns = [
    path("display",display,name="display"),
    path("create",create,name="create")
]