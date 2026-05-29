from django.urls import path
from .views import *

urlpatterns = [
    path('cart/', CartView.as_view()),
    path('wishlist/', WishlistView.as_view()),
    path('orders/', OrderView.as_view()),
    path('orders/<int:id>/', OrderView.as_view()),
    path('order-items/', OrderItemView.as_view()),
]
