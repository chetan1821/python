from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Product, Category, Wishlist, WishlistItem
from .forms import ProductFilterForm
from reviews.models import Review


def home(request):
    """
    Home page view with featured products.
    """
    # Get featured products
    featured_products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    
    # Get all categories
    categories = Category.objects.filter(is_active=True)
    
    # Get latest products
    latest_products = Product.objects.filter(is_active=True).order_by('-created_at')[:8]
    
    context = {
        'featured_products': featured_products,
        'categories': categories,
        'latest_products': latest_products,
        'page_title': 'Home',
    }
    return render(request, 'products/home.html', context)


def product_list(request):
    """
    Product listing page with filtering and pagination.
    """
    # Get all active products
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)
    
    # Apply filters
    form = ProductFilterForm(request.GET)
    
    # Search filter
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(sku__icontains=search_query)
        )
    
    # Category filter
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)
    
    # Price filter
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    
    if price_min:
        products = products.filter(price__gte=price_min)
    if price_max:
        products = products.filter(price__lte=price_max)
    
    # Sorting
    sort_by = request.GET.get('sort_by', '-created_at')
    if sort_by:
        products = products.order_by(sort_by)
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'products': page_obj.object_list,
        'categories': categories,
        'form': form,
        'search_query': search_query,
        'page_title': 'Products',
    }
    return render(request, 'products/product_list.html', context)


def category_products(request, category_slug):
    """
    View products by category.
    """
    category = get_object_or_404(Category, slug=category_slug, is_active=True)
    products = category.products.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)
    
    # Apply filters
    form = ProductFilterForm(request.GET)
    
    # Search within category
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Price filter
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    
    if price_min:
        products = products.filter(price__gte=price_min)
    if price_max:
        products = products.filter(price__lte=price_max)
    
    # Sorting
    sort_by = request.GET.get('sort_by', '-created_at')
    if sort_by:
        products = products.order_by(sort_by)
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'page_obj': page_obj,
        'products': page_obj.object_list,
        'categories': categories,
        'form': form,
        'search_query': search_query,
        'page_title': f'{category.name} Products',
    }
    return render(request, 'products/category_products.html', context)


def product_detail(request, product_id):
    """
    Detailed product view with images, reviews, and related products.
    """
    product = get_object_or_404(Product, id=product_id, is_active=True)
    
    # Get product images
    images = product.images.all()
    
    # Get reviews
    reviews = Review.objects.filter(product=product, is_approved=True).order_by('-created_at')
    
    # Get related products (same category)
    related_products = Product.objects.filter(
        category=product.category,
        is_active=True
    ).exclude(id=product.id)[:4]
    
    # Check if product is in user's wishlist
    is_in_wishlist = False
    if request.user.is_authenticated:
        is_in_wishlist = WishlistItem.objects.filter(
            wishlist__user=request.user,
            product=product
        ).exists()
    
    context = {
        'product': product,
        'images': images,
        'reviews': reviews,
        'related_products': related_products,
        'is_in_wishlist': is_in_wishlist,
        'page_title': product.name,
    }
    return render(request, 'products/product_detail.html', context)


@login_required(login_url='accounts:login')
def add_to_wishlist(request, product_id):
    """
    Add product to wishlist (AJAX request).
    """
    product = get_object_or_404(Product, id=product_id)
    
    try:
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        wishlist_item, created = WishlistItem.objects.get_or_create(
            wishlist=wishlist,
            product=product
        )
        
        if created:
            messages.success(request, f'{product.name} added to wishlist!')
        else:
            messages.info(request, f'{product.name} is already in your wishlist.')
    except Exception as e:
        messages.error(request, f'Error: {str(e)}')
    
    return redirect('products:product_detail', product_id=product.id)


@login_required(login_url='accounts:login')
def remove_from_wishlist(request, product_id):
    """
    Remove product from wishlist.
    """
    product = get_object_or_404(Product, id=product_id)
    
    try:
        wishlist = request.user.wishlist
        WishlistItem.objects.filter(wishlist=wishlist, product=product).delete()
        messages.success(request, f'{product.name} removed from wishlist!')
    except Exception as e:
        messages.error(request, f'Error: {str(e)}')
    
    return redirect('products:product_detail', product_id=product.id)


@login_required(login_url='accounts:login')
def wishlist_view(request):
    """
    View user's wishlist.
    """
    try:
        wishlist = request.user.wishlist
        wishlist_items = wishlist.items.all()
    except Wishlist.DoesNotExist:
        wishlist = None
        wishlist_items = []
    
    context = {
        'wishlist': wishlist,
        'wishlist_items': wishlist_items,
        'page_title': 'My Wishlist',
    }
    return render(request, 'products/wishlist.html', context)


def search_products(request):
    """
    Search products by query.
    """
    query = request.GET.get('q', '')
    products = Product.objects.filter(is_active=True)
    
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(sku__icontains=query)
        )
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'products': page_obj.object_list,
        'query': query,
        'page_title': f'Search Results: {query}',
    }
    return render(request, 'products/search_results.html', context)


# Error handlers
def page_not_found(request, exception):
    """Handle 404 errors."""
    return render(request, '404.html', status=404)


def server_error(request):
    """Handle 500 errors."""
    return render(request, '500.html', status=500)
