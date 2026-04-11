from django.db import models
from django.contrib.auth.models import User
from products.models import Product
import uuid


class Cart(models.Model):
    """
    Shopping cart model for storing user's selected products.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
    
    def __str__(self):
        return f"{self.user.username}'s Cart"
    
    @property
    def total_items(self):
        """Get total number of items in cart."""
        return sum(item.quantity for item in self.items.all())
    
    @property
    def total_price(self):
        """Calculate total price of all items in cart."""
        return sum(item.get_total() for item in self.items.all())
    
    @property
    def total_discount(self):
        """Calculate total discount amount."""
        return sum(item.get_discount() for item in self.items.all())


class CartItem(models.Model):
    """
    Individual items in the shopping cart.
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price at time of adding
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"
        unique_together = ('cart', 'product')
    
    def __str__(self):
        return f"{self.product.name} x{self.quantity}"
    
    def get_total(self):
        """Calculate total price for this item."""
        # Use discounted price if available
        effective_price = self.product.discounted_price
        return effective_price * self.quantity
    
    def get_discount(self):
        """Calculate discount amount for this item."""
        if self.product.discount_price:
            discount_per_item = self.product.price - self.product.discount_price
            return discount_per_item * self.quantity
        return 0
    
    def save(self, *args, **kwargs):
        """Store the price at the time of adding to cart."""
        if not self.pk:  # Only on creation
            self.price = self.product.discounted_price
        super().save(*args, **kwargs)


class Order(models.Model):
    """
    Customer order model.
    """
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('cod', 'Cash on Delivery'),
        ('razorpay', 'Razorpay'),
        ('stripe', 'Stripe'),
    ]
    
    # Order Information
    order_number = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders')
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    
    # Customer Details
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    
    # Shipping Address
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    
    # Payment Details
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='cod')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # Additional Info
    notes = models.TextField(blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Order {self.order_number}"
    
    def save(self, *args, **kwargs):
        """Generate unique order number on creation."""
        if not self.order_number:
            self.order_number = f"ORD-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)
    
    @property
    def subtotal(self):
        """Calculate subtotal before tax and shipping."""
        return self.total_amount - self.tax_amount - self.shipping_cost


class OrderItem(models.Model):
    """
    Individual items in an order.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price at time of order
    
    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"
    
    def __str__(self):
        return f"{self.product.name} x{self.quantity}"
    
    def get_total(self):
        """Calculate total for this order item."""
        return self.price * self.quantity
