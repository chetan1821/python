from django.urls import path
from auth_app.views import *
urlpatterns = [
    path('',login_page,name="login"),
    path('reg_user',reg_user,name="reg"),
    path('index',index,name="index"),
    path("logout",user_logout,name="logout")

]
