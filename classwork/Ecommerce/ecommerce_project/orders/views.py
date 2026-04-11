from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db import transaction
from products.models import Product
from .models import Cart, CartItem, Order, OrderItem
from .forms import CheckoutForm


@login_required(login_url='accounts:login')
def view_cart(request):
    """
    Display shopping cart with all items.
    """
    try:
        cart = request.user.cart
        cart_items = cart.items.all()
    except Cart.DoesNotExist:
        cart = None
        cart_items = []
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'page_title': 'Shopping Cart',
    }
    return render(request, 'orders/cart.html', context)


@login_required(login_url='accounts:login')
def add_to_cart(request, product_id):
    """
    Add product to cart. Can be called via AJAX or regular request.
    """
    product = get_object_or_404(Product, id=product_id, is_active=True)
    
    # Get or create cart
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Get quantity from request
    quantity = int(request.POST.get('quantity', 1))
    
    # Check stock
    if quantity > product.stock:
        messages.error(request, f'Only {product.stock} items available in stock.')
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'message': f'Only {product.stock} available'})
        return redirect('products:product_detail', product_id=product.id)
    
    # Get or create cart item
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': quantity}
    )
    
    if not created:
        # Update quantity if item already exists
        if cart_item.quantity + quantity <= product.stock:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            messages.warning(request, f'Only {product.stock} items available. Updated quantity.')
            cart_item.quantity = product.stock
            cart_item.save()
    
    messages.success(request, f'{product.name} added to cart!')
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'message': f'{product.name} added to cart!',
            'cart_total_items': cart.total_items,
            'cart_total_price': str(cart.total_price),
        })
    
    return redirect('orders:view_cart')


@login_required(login_url='accounts:login')
def update_cart_item(request, item_id):
    """
    Update quantity of cart item via AJAX.
    """
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        
        # Check stock
        if quantity > cart_item.product.stock:
            return JsonResponse({
                'success': False,
                'message': f'Only {cart_item.product.stock} items available'
            })
        
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            
            cart = cart_item.cart
            return JsonResponse({
                'success': True,
                'item_total': str(cart_item.get_total()),
                'cart_total': str(cart.total_price),
                'cart_items': cart.total_items,
            })
        else:
            cart_item.delete()
            cart = Cart.objects.get(user=request.user)
            return JsonResponse({
                'success': True,
                'cart_total': str(cart.total_price),
                'cart_items': cart.total_items,
                'item_deleted': True,
            })
    
    return JsonResponse({'success': False, 'message': 'Invalid request'})


@login_required(login_url='accounts:login')
def remove_from_cart(request, item_id):
    """
    Remove item from cart.
    """
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    product_name = cart_item.product.name
    cart_item.delete()
    
    messages.success(request, f'{product_name} removed from cart.')
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        cart = Cart.objects.get(user=request.user)
        return JsonResponse({
            'success': True,
            'cart_total': str(cart.total_price),
            'cart_items': cart.total_items,
        })
    
    return redirect('orders:view_cart')


@login_required(login_url='accounts:login')
def checkout(request):
    """
    Checkout view - process order placement.
    """
    try:
        cart = request.user.cart
        cart_items = cart.items.all()
        
        if not cart_items.exists():
            messages.warning(request, 'Your cart is empty!')
            return redirect('products:product_list')
    except Cart.DoesNotExist:
        messages.warning(request, 'Your cart is empty!')
        return redirect('products:product_list')
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    # Create order
                    order = form.save(commit=False)
                    order.user = request.user
                    order.total_amount = cart.total_price
                    order.save()
                    
                    # Create order items from cart
                    for cart_item in cart_items:
                        OrderItem.objects.create(
                            order=order,
                            product=cart_item.product,
                            quantity=cart_item.quantity,
                            price=cart_item.price,
                        )
                    
                    # Clear cart
                    cart.items.all().delete()
                    
                    messages.success(request, f'Order {order.order_number} placed successfully!')
                    return redirect('orders:order_confirmation', order_id=order.id)
            except Exception as e:
                messages.error(request, f'Error placing order: {str(e)}')
    else:
        # Pre-fill form with user data
        initial_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        }
        
        # Add profile data if available
        if hasattr(request.user, 'profile'):
            profile = request.user.profile
            initial_data.update({
                'phone': profile.phone,
                'address': profile.address,
                'city': profile.city,
                'state': profile.state,
                'country': profile.country,
                'postal_code': profile.postal_code,
            })
        
        form = CheckoutForm(initial=initial_data)
    
    context = {
        'form': form,
        'cart': cart,
        'cart_items': cart_items,
        'page_title': 'Checkout',
    }
    return render(request, 'orders/checkout.html', context)


@login_required(login_url='accounts:login')
def order_confirmation(request, order_id):
    """
    Order confirmation page.
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = order.items.all()
    
    context = {
        'order': order,
        'order_items': order_items,
        'page_title': 'Order Confirmation',
    }
    return render(request, 'orders/order_confirmation.html', context)


@login_required(login_url='accounts:login')
def order_history(request):
    """
    Display user's order history.
    """
    orders = request.user.orders.all().order_by('-created_at')
    
    context = {
        'orders': orders,
        'page_title': 'Order History',
    }
    return render(request, 'orders/order_history.html', context)


@login_required(login_url='accounts:login')
def order_detail(request, order_id):
    """
    Display detailed order information.
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = order.items.all()
    
    context = {
        'order': order,
        'order_items': order_items,
        'page_title': f'Order {order.order_number}',
    }
    return render(request, 'orders/order_detail.html', context)


@login_required(login_url='accounts:login')
@require_http_methods(["POST"])
def cancel_order(request, order_id):
    """
    Cancel order (only if status is pending).
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    if order.status != 'pending':
        messages.error(request, 'Can only cancel pending orders.')
    else:
        order.status = 'cancelled'
        order.save()
        messages.success(request, f'Order {order.order_number} cancelled successfully.')
    
    return redirect('orders:order_detail', order_id=order.id)
