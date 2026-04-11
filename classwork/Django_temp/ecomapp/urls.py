from django.urls import path
from ecomapp.views import *
urlpatterns = [
    path('',index,name="index"),
    path('shop/',shop,name="shop"),
    path('about/',about,name="about"),
    path('services/',services,name="services"),
    path('blog/',blog,name="blog"),
    path('contact/',contact,name="contact"),
    path('cart/',cart,name="cart"),
    path('checkout/',checkout,name="checkout"),
    path('thankyou/',thankyou,name="thankyou"),
]
