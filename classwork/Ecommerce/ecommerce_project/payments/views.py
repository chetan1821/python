from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from orders.models import Order
from .models import Payment, PaymentLog
from .forms import PaymentForm


@login_required(login_url='accounts:login')
def initiate_payment(request, order_id):
    """
    Initiate payment for an order.
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    # If payment method is Cash on Delivery, mark order as confirmed
    if order.payment_method == 'cod':
        order.status = 'confirmed'
        order.payment_status = 'completed'
        order.save()
        
        PaymentLog.objects.create(
            order=order,
            action='cod_selected',
            message='Cash on Delivery selected. Order confirmed.'
        )
        
        messages.success(request, 'Order confirmed with Cash on Delivery payment method.')
        return redirect('orders:order_confirmation', order_id=order.id)
    
    # For other payment methods, create payment record
    try:
        payment = Payment.objects.create(
            order=order,
            amount=order.total_amount,
            payment_method=order.payment_method
        )
        
        # Log payment initiation
        PaymentLog.objects.create(
            payment=payment,
            action='initiated',
            message=f'Payment initiated via {order.payment_method}'
        )
        
        if order.payment_method == 'razorpay':
            return redirect('payments:razorpay_payment', payment_id=payment.id)
        elif order.payment_method == 'stripe':
            return redirect('payments:stripe_payment', payment_id=payment.id)
    except Exception as e:
        messages.error(request, f'Error initiating payment: {str(e)}')
    
    return redirect('orders:order_detail', order_id=order.id)


@login_required(login_url='accounts:login')
def razorpay_payment(request, payment_id):
    """
    Razorpay payment gateway integration.
    This is a dummy implementation. In production, integrate with actual Razorpay API.
    """
    payment = get_object_or_404(Payment, id=payment_id)
    order = payment.order
    
    try:
        import razorpay
        
        # Initialize Razorpay client
        client = razorpay.Client(auth=('RAZORPAY_KEY_ID', 'RAZORPAY_KEY_SECRET'))
        
        # Create Razorpay order
        razorpay_order = client.order.create({
            'amount': int(order.total_amount * 100),  # Amount in paise
            'currency': 'INR',
            'receipt': payment.transaction_id
        })
        
        context = {
            'order': order,
            'payment': payment,
            'razorpay_order': razorpay_order,
            'page_title': 'Razorpay Payment',
        }
        return render(request, 'payments/razorpay.html', context)
    except Exception as e:
        messages.error(request, f'Error processing payment: {str(e)}')
        return redirect('orders:order_detail', order_id=order.id)


@login_required(login_url='accounts:login')
def razorpay_callback(request):
    """
    Razorpay payment callback handler.
    """
    if request.method == 'POST':
        try:
            payment_id = request.POST.get('razorpay_payment_id')
            order_id = request.POST.get('razorpay_order_id')
            signature = request.POST.get('razorpay_signature')
            
            # Verify signature (implement in production)
            # For now, mark payment as completed
            payment = Payment.objects.get(
                order__payment_method='razorpay',
                response_data__razorpay_order_id=order_id
            )
            
            payment.status = 'completed'
            payment.response_data = {
                'razorpay_payment_id': payment_id,
                'razorpay_order_id': order_id,
            }
            payment.save()
            
            # Update order
            payment.order.payment_status = 'completed'
            payment.order.status = 'confirmed'
            payment.order.save()
            
            # Log payment
            PaymentLog.objects.create(
                payment=payment,
                action='success',
                message='Payment completed successfully via Razorpay'
            )
            
            messages.success(request, 'Payment completed successfully!')
            return redirect('orders:order_confirmation', order_id=payment.order.id)
        except Exception as e:
            messages.error(request, f'Payment verification failed: {str(e)}')
            return redirect('products:home')
    
    return redirect('products:home')


@login_required(login_url='accounts:login')
def stripe_payment(request, payment_id):
    """
    Stripe payment gateway integration.
    This is a dummy implementation. In production, integrate with actual Stripe API.
    """
    payment = get_object_or_404(Payment, id=payment_id)
    order = payment.order
    
    context = {
        'order': order,
        'payment': payment,
        'stripe_public_key': 'pk_test_dummy_key',
        'page_title': 'Stripe Payment',
    }
    return render(request, 'payments/stripe.html', context)


@login_required(login_url='accounts:login')
def payment_success(request, payment_id):
    """
    Handle successful payment.
    """
    payment = get_object_or_404(Payment, id=payment_id)
    order = payment.order
    
    # Verify payment is completed
    if payment.status == 'completed':
        messages.success(request, 'Payment completed successfully!')
        return redirect('orders:order_confirmation', order_id=order.id)
    
    messages.error(request, 'Payment not verified.')
    return redirect('orders:order_detail', order_id=order.id)


@login_required(login_url='accounts:login')
def payment_failure(request, payment_id):
    """
    Handle failed payment.
    """
    payment = get_object_or_404(Payment, id=payment_id)
    order = payment.order
    
    payment.status = 'failed'
    payment.error_message = 'Payment failed by user'
    payment.save()
    
    PaymentLog.objects.create(
        payment=payment,
        action='failed',
        message='Payment failed'
    )
    
    messages.error(request, 'Payment failed. Please try again.')
    return redirect('orders:checkout')
