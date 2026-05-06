from django.urls import path
from productapp.views import *
urlpatterns = [
    path("product",ProductView.as_view()),
    path("product/<id>",ProductRetrive.as_view()),
    path("category",CategoryView.as_view()),
    path("category/<id>",CategoryRetrive.as_view()),

    path("products/category/<id>",product_by_category)
]
