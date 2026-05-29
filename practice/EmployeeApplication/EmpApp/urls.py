from django.urls import path
from EmpApp.views import *
urlpatterns = [
    path("",index,name="index"),
    path("delete",delete,name="delete"),
    path("update",update,name="update"),
    path('send-email/', send_email),
    path('send/', send_otp, name='send_otp'),
    path('verify/', verify_otp, name='verify_otp'),
]
