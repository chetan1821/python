from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',index,name="index"),
    path("addproduct",add_product,name="addproduct"),
    path('delete',delete,name="delete"),
    path('update',update,name="update")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
