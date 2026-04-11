from django.db import models
from orders.models import Order
import uuid


class Payment(models.Model):
    """
    Payment model for tracking payment transactions.
    """
    PAYMENT_METHOD_CHOICES = [
        ('razorpay', 'Razorpay'),
        ('stripe', 'Stripe'),
        ('paypal', 'PayPal'),
        ('cod', 'Cash on Delivery'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('initiated', 'Initiated'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]
    
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    transaction_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Additional info
    response_data = models.JSONField(blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Payment for {self.order.order_number}"
    
    def save(self, *args, **kwargs):
        """Generate transaction ID if not provided."""
        if not self.transaction_id:
            self.transaction_id = f"TXN-{uuid.uuid4().hex[:12].upper()}"
        super().save(*args, **kwargs)


class PaymentLog(models.Model):
    """
    Log of payment actions for audit trail.
    """
    ACTION_CHOICES = [
        ('initiated', 'Payment Initiated'),
        ('processing', 'Processing Payment'),
        ('success', 'Payment Successful'),
        ('failed', 'Payment Failed'),
        ('refund_initiated', 'Refund Initiated'),
        ('refund_completed', 'Refund Completed'),
    ]
    
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='logs')
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    message = models.TextField()
    response_data = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Payment Log"
        verbose_name_plural = "Payment Logs"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.payment.transaction_id} - {self.action}"
