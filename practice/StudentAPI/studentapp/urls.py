from django.urls import path
from studentapp.views import *
urlpatterns = [
      path("all/",StudentView.as_view()),
      path("all/<id>",StudentUpdate.as_view())
] 
