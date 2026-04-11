from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from products.models import Product
from orders.models import Order, OrderItem
from .models import Review
from .forms import ReviewForm


@login_required(login_url='accounts:login')
def add_review(request, product_id):
    """
    Add or update a review for a product.
    """
    product = get_object_or_404(Product, id=product_id)
    
    # Check if user has purchased this product
    has_purchased = OrderItem.objects.filter(
        order__user=request.user,
        product=product,
        order__status__in=['delivered', 'confirmed']
    ).exists()
    
    if not has_purchased:
        messages.warning(request, 'You can only review products you have purchased and received.')
        return redirect('products:product_detail', product_id=product.id)
    
    # Get or create review
    try:
        review = Review.objects.get(product=product, user=request.user)
        is_edit = True
    except Review.DoesNotExist:
        review = None
        is_edit = False
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            try:
                with transaction.atomic():
                    review = form.save(commit=False)
                    review.product = product
                    review.user = request.user
                    review.is_approved = False  # Reviews need approval
                    review.save()
                    
                    if is_edit:
                        messages.success(request, 'Your review has been updated!')
                    else:
                        messages.success(request, 'Your review has been submitted for approval!')
                    
                    return redirect('products:product_detail', product_id=product.id)
            except Exception as e:
                messages.error(request, f'Error submitting review: {str(e)}')
    else:
        form = ReviewForm(instance=review)
    
    context = {
        'form': form,
        'product': product,
        'is_edit': is_edit,
        'page_title': f'Review {product.name}',
    }
    return render(request, 'reviews/add_review.html', context)


@login_required(login_url='accounts:login')
def delete_review(request, review_id):
    """
    Delete a review (only by author or admin).
    """
    review = get_object_or_404(Review, id=review_id)
    
    if review.user != request.user and not request.user.is_staff:
        messages.error(request, 'You do not have permission to delete this review.')
        return redirect('products:product_detail', product_id=review.product.id)
    
    product_id = review.product.id
    review.delete()
    messages.success(request, 'Review deleted successfully!')
    
    return redirect('products:product_detail', product_id=product_id)


@login_required(login_url='accounts:login')
def my_reviews(request):
    """
    Display user's reviews.
    """
    reviews = Review.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'reviews': reviews,
        'page_title': 'My Reviews',
    }
    return render(request, 'reviews/my_reviews.html', context)
