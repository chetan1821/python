from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",index,name="index"),
    path("login/",login_page,name="login"),
    path("reg/",reg,name="reg"),
    path("logout/",user_logout,name="logout"),
    path("doctor/",doctor_info,name="doctor"),
    path("profile/",profile,name="profile"),
     path('add-doctor/',add_doctor, name="add_doctor"),

    path('update-doctor/<int:id>/',update_doctor, name="update_doctor"),

    path('delete-doctor/<int:id>/',delete_doctor, name="delete_doctor"),
    path('contact/',contact,name="contact")

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
