from django.urls import path
from myapp.views import *
urlpatterns = [
    path('',index,name="index"),
    path('employee/',employee,name="employee"),
   
    path('login/',login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path('product/',product, name='product'),
    path('products/',product_list, name='product_list'),
    path('delete-product/<int:id>/',delete_product, name='delete_product'),
]

