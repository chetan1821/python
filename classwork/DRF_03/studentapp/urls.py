from django.urls import path
from studentapp.views import *
urlpatterns = [
    path("get/",get_student,name="get"),
    path("post/",post_student,name="post"),
    path("put/<id>",put_student,name="put"),
    path("delete/<id>",delete_student,name="delete")
]

