from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",index,name="index"),
    path("login/",login_page,name="login"),
    path("reg/",reg,name="reg"),
    path("logout",user_logout,name="logout"),
    path("doctor",doctor_info,name="doctor")

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
