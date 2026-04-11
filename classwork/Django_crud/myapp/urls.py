from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",student,name="student"),
    path("employee/",employee,name="employee"),
    path("product/",product,name="product"),
    path('delete/',delete,name="delete"),
    path('del_emp/',del_emp,name='del_emp'),
    path('del_product/',del_product,name='del_product'),
]
