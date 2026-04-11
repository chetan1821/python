from django.urls import path
from CRUD_APP.views import *
from django.conf.urls.static import *
from django.conf import settings
urlpatterns = [
    path('',index,name="index"),
    path('delete',delete,name="delete"),
    path('update',update,name="update"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

