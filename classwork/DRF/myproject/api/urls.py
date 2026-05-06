from django.urls import path
from .views import *

urlpatterns = [
    path('get/', get_api),
    path('post/', post_api),
    path('put/', put_api),
    path('delete/', delete_api),
]