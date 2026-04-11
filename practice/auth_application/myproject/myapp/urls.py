from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', login_page, name="login_page"),
    path('register/', register, name="register"),
    path('dashboard/', dashboard, name="dashboard"),
    path('logout/',logout_user,name='logout'),
]