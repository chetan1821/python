from django.urls import path
from products.views import *
urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('products/', ProductView.as_view()),
]