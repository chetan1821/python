from django.urls import path
from myapp.views import *
urlpatterns = [
     path("get/",get_api,name="get"),
     path("post/",post_api,name="post"),
     path("put/",put_api,name="put"),
     path("delete/",del_api,name="delete")
]
