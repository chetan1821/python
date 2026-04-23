from django.urls import path
from myapp.views import *
urlpatterns = [
    path("",index,name="index"),
    path("display",display,name="display"),
    path("adduser",add_user,name="adduser"),
    path("deleteuser",delete_user,name="deleteuser"),
    path("edituser",edit_user,name="edituser"),
    path("updateuser",update_user,name="updateuser"),
    path("search",search,name="search")

]
