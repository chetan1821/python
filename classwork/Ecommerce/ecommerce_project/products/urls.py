from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # Home and listing
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.category_products, name='category_products'),
    
    # Product detail
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    
    # Search
    path('search/', views.search_products, name='search_products'),
    
    # Wishlist
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]
