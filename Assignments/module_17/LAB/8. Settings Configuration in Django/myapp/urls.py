from django.urls import path
from myapp.views import *

urlpatterns = [
    path('doctor/',doctordata.as_view())
]
