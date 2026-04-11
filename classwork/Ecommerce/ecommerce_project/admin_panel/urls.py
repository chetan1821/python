from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    # Dashboard
    path('', views.admin_dashboard, name='dashboard'),
    
    # Products
    path('products/', views.manage_products, name='manage_products'),
    
    # Orders
    path('orders/', views.manage_orders, name='manage_orders'),
    path('orders/<int:order_id>/', views.order_detail_admin, name='order_detail_admin'),
    
    # Users
    path('users/', views.manage_users, name='manage_users'),
    
    # Reviews
    path('reviews/', views.manage_reviews, name='manage_reviews'),
    
    # Categories
    path('categories/', views.manage_categories, name='manage_categories'),
]
