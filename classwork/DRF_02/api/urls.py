from django.urls import path
from api.views import *
urlpatterns = [
    path("students",studentView),
    path("put/<id>",put_student,name="put"),
    path("delete/<id>",delete_student,name="delete")
]
