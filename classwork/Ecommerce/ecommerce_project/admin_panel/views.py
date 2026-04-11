from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.db.models import Sum, Count, Q
from django.utils import timezone
from datetime import timedelta
from products.models import Product, Category
from accounts.models import UserProfile
from orders.models import Order, OrderItem
from reviews.models import Review
from django.contrib.auth.models import User
from django.core.paginator import Paginator


def is_admin(user):
    """Check if user is admin."""
    return user.is_staff or user.is_superuser


@user_passes_test(is_admin)
def admin_dashboard(request):
    """
    Admin dashboard with key metrics and analytics.
    """
    # Get date range for analytics
    today = timezone.now()
    last_30_days = today - timedelta(days=30)
    
    # Key metrics
    total_orders = Order.objects.count()
    total_revenue = Order.objects.filter(payment_status='completed').aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    total_products = Product.objects.count()
    total_users = User.objects.count()
    
    # Recent 30 days metrics
    orders_last_30_days = Order.objects.filter(created_at__gte=last_30_days).count()
    revenue_last_30_days = Order.objects.filter(
        payment_status='completed',
        created_at__gte=last_30_days
    ).aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    
    # Order status breakdown
    pending_orders = Order.objects.filter(status='pending').count()
    confirmed_orders = Order.objects.filter(status='confirmed').count()
    shipped_orders = Order.objects.filter(status='shipped').count()
    delivered_orders = Order.objects.filter(status='delivered').count()
    
    # Recent orders
    recent_orders = Order.objects.all().order_by('-created_at')[:5]
    
    # Top products
    top_products = Product.objects.annotate(
        total_sold=Count('orderitem')
    ).order_by('-total_sold')[:5]
    
    # Top categories
    top_categories = Category.objects.annotate(
        product_count=Count('products'),
        total_sold=Count('products__orderitem')
    ).order_by('-total_sold')[:5]
    
    context = {
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'total_products': total_products,
        'total_users': total_users,
        'orders_last_30_days': orders_last_30_days,
        'revenue_last_30_days': revenue_last_30_days,
        'pending_orders': pending_orders,
        'confirmed_orders': confirmed_orders,
        'shipped_orders': shipped_orders,
        'delivered_orders': delivered_orders,
        'recent_orders': recent_orders,
        'top_products': top_products,
        'top_categories': top_categories,
        'page_title': 'Admin Dashboard',
    }
    return render(request, 'admin_panel/dashboard.html', context)


@user_passes_test(is_admin)
def manage_products(request):
    """
    Manage products - list, add, edit, delete.
    """
    if request.method == 'POST':
        action = request.POST.get('action')
        product_id = request.POST.get('product_id')
        
        if action == 'delete':
            product = get_object_or_404(Product, id=product_id)
            product.delete()
            messages.success(request, 'Product deleted successfully!')
            return redirect('admin_panel:manage_products')
        
        elif action == 'toggle_active':
            product = get_object_or_404(Product, id=product_id)
            product.is_active = not product.is_active
            product.save()
            status = 'activated' if product.is_active else 'deactivated'
            messages.success(request, f'Product {status} successfully!')
            return redirect('admin_panel:manage_products')
    
    products = Product.objects.all().order_by('-created_at')
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(sku__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(products, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'products': page_obj.object_list,
        'search_query': search_query,
        'page_title': 'Manage Products',
    }
    return render(request, 'admin_panel/manage_products.html', context)


@user_passes_test(is_admin)
def manage_orders(request):
    """
    Manage orders - view, update status, delete.
    """
    if request.method == 'POST':
        action = request.POST.get('action')
        order_id = request.POST.get('order_id')
        
        if action == 'update_status':
            order = get_object_or_404(Order, id=order_id)
            new_status = request.POST.get('status')
            order.status = new_status
            order.save()
            messages.success(request, f'Order status updated to {new_status}!')
            return redirect('admin_panel:manage_orders')
    
    orders = Order.objects.all().order_by('-created_at')
    
    # Filter by status
    status_filter = request.GET.get('status', '')
    if status_filter:
        orders = orders.filter(status=status_filter)
    
    # Pagination
    paginator = Paginator(orders, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'orders': page_obj.object_list,
        'status_filter': status_filter,
        'statuses': Order.ORDER_STATUS_CHOICES,
        'page_title': 'Manage Orders',
    }
    return render(request, 'admin_panel/manage_orders.html', context)


@user_passes_test(is_admin)
def order_detail_admin(request, order_id):
    """
    View detailed order information from admin panel.
    """
    order = get_object_or_404(Order, id=order_id)
    order_items = order.items.all()
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status:
            order.status = new_status
            order.save()
            messages.success(request, f'Order status updated to {new_status}!')
            return redirect('admin_panel:order_detail_admin', order_id=order.id)
    
    context = {
        'order': order,
        'order_items': order_items,
        'statuses': Order.ORDER_STATUS_CHOICES,
        'page_title': f'Order {order.order_number}',
    }
    return render(request, 'admin_panel/order_detail.html', context)


@user_passes_test(is_admin)
def manage_users(request):
    """
    Manage users - view and manage user accounts.
    """
    users = User.objects.all().order_by('-date_joined')
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(first_name__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(users, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'users': page_obj.object_list,
        'search_query': search_query,
        'page_title': 'Manage Users',
    }
    return render(request, 'admin_panel/manage_users.html', context)


@user_passes_test(is_admin)
def manage_reviews(request):
    """
    Manage product reviews - approve, reject, delete.
    """
    if request.method == 'POST':
        action = request.POST.get('action')
        review_id = request.POST.get('review_id')
        
        review = get_object_or_404(Review, id=review_id)
        
        if action == 'approve':
            review.is_approved = True
            review.save()
            messages.success(request, 'Review approved!')
        elif action == 'reject':
            review.delete()
            messages.success(request, 'Review deleted!')
        
        return redirect('admin_panel:manage_reviews')
    
    # Get pending reviews
    pending_reviews = Review.objects.filter(is_approved=False).order_by('-created_at')
    
    # Pagination
    paginator = Paginator(pending_reviews, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'reviews': page_obj.object_list,
        'page_title': 'Manage Reviews',
    }
    return render(request, 'admin_panel/manage_reviews.html', context)


@user_passes_test(is_admin)
def manage_categories(request):
    """
    Manage product categories.
    """
    if request.method == 'POST':
        action = request.POST.get('action')
        category_id = request.POST.get('category_id')
        
        if action == 'delete':
            category = get_object_or_404(Category, id=category_id)
            category.delete()
            messages.success(request, 'Category deleted successfully!')
            return redirect('admin_panel:manage_categories')
    
    categories = Category.objects.all().order_by('name')
    
    # Pagination
    paginator = Paginator(categories, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'categories': page_obj.object_list,
        'page_title': 'Manage Categories',
    }
    return render(request, 'admin_panel/manage_categories.html', context)
