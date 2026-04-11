from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    """
    Product category model for organizing products.
    """
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/%Y/%m/%d/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products:category_products', args=[self.slug])


class Product(models.Model):
    """
    Product model with detailed information.
    """
    # Basic Information
    name = models.CharField(max_length=300)
    sku = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    long_description = models.TextField(blank=True, null=True)
    
    # Pricing
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0)])
    
    # Stock Management
    stock = models.PositiveIntegerField(default=0)
    
    # Status
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.id])
    
    @property
    def discounted_price(self):
        """Calculate discounted price if available."""
        if self.discount_price:
            return self.discount_price
        return self.price
    
    @property
    def discount_percentage(self):
        """Calculate discount percentage."""
        if self.discount_price:
            discount = ((self.price - self.discount_price) / self.price) * 100
            return int(discount)
        return 0
    
    @property
    def is_in_stock(self):
        """Check if product is in stock."""
        return self.stock > 0
    
    @property
    def average_rating(self):
        """Calculate average rating from reviews."""
        from reviews.models import Review
        reviews = Review.objects.filter(product=self, is_approved=True)
        if reviews.exists():
            total_rating = sum(review.rating for review in reviews)
            return round(total_rating / reviews.count(), 1)
        return 0
    
    @property
    def review_count(self):
        """Count approved reviews."""
        from reviews.models import Review
        return Review.objects.filter(product=self, is_approved=True).count()


class ProductImage(models.Model):
    """
    Multiple images for each product.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    alt_text = models.CharField(max_length=200, blank=True, null=True)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"
        ordering = ['-is_primary', 'created_at']
    
    def __str__(self):
        return f"Image for {self.product.name}"
    
    def save(self, *args, **kwargs):
        """Ensure only one primary image per product."""
        if self.is_primary:
            ProductImage.objects.filter(product=self.product, is_primary=True).update(is_primary=False)
        super().save(*args, **kwargs)


class Wishlist(models.Model):
    """
    User wishlist for saving favorite products.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist')
    products = models.ManyToManyField(Product, through='WishlistItem', related_name='wishlisted_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"
    
    def __str__(self):
        return f"{self.user.username}'s Wishlist"


class WishlistItem(models.Model):
    """
    Through model for Wishlist and Product many-to-many relationship.
    """
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Wishlist Item"
        verbose_name_plural = "Wishlist Items"
        unique_together = ('wishlist', 'product')
    
    def __str__(self):
        return f"{self.product.name} in {self.wishlist.user.username}'s Wishlist"
