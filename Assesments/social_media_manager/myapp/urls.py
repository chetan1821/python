from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',list_profiles, name='list_profiles'),
    path('create/',create_profile, name='create_profile'),
    path('export/',export_csv, name='export_csv'),
    path('profile/<int:pk>/',view_profile, name='view_profile'),
    path('profile/<int:pk>/edit/',update_profile, name='update_profile'),
    path('profile/<int:pk>/delete/',delete_profile, name='delete_profile'),
]
