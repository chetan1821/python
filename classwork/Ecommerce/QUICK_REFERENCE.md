# EzyMart - Quick Reference Guide

## Common Commands

### Django Management Commands

```bash
# Create superuser (admin account)
python manage.py createsuperuser

# Make migrations (after model changes)
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Run development server
python manage.py runserver

# Run tests
python manage.py test

# Collect static files (for production)
python manage.py collectstatic

# Create a new app
python manage.py startapp app_name

# Open Django shell for database queries
python manage.py shell
```

## Database Queries

### In Django Shell

```python
python manage.py shell

# Add products
from products.models import Product, Category

category = Category.objects.create(
    name="Electronics",
    slug="electronics",
    description="Electronic devices"
)

Product.objects.create(
    name="Wireless Headphones",
    sku="PROD-001",
    category=category,
    description="High-quality wireless headphones",
    price=2999,
    discount_price=2499,
    stock=50
)

# Query products
products = Product.objects.all()
featured = Product.objects.filter(is_featured=True)

# Get specific product
product = Product.objects.get(id=1)
print(product.name)

# Update product
product.price = 3000
product.save()

# Delete product
product.delete()
```

## File Locations

| File | Purpose |
|------|---------|
| `ecommerce/settings.py` | Project settings |
| `ecommerce/urls.py` | Main URL routing |
| `accounts/models.py` | User models |
| `products/models.py` | Product models |
| `orders/models.py` | Cart & Order models |
| `templates/base.html` | Base template |
| `static/css/custom.css` | Custom styling |

## Adding a New Feature

### Step 1: Create Model
```python
# In app/models.py
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
```

### Step 2: Create Views
```python
# In app/views.py
from django.shortcuts import render
from .models import MyModel

def my_view(request):
    items = MyModel.objects.all()
    return render(request, 'app/template.html', {'items': items})
```

### Step 3: Add URLs
```python
# In app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='view_name'),
]
```

### Step 4: Create Template
```html
<!-- In templates/app/template.html -->
{% extends 'base.html' %}
{% block content %}
    <!-- Your HTML here -->
{% endblock %}
```

### Step 5: Register in Apps
```python
# In app/apps.py
class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
```

Then add to `INSTALLED_APPS` in settings.py:
```python
INSTALLED_APPS = [
    ...
    'myapp.apps.MyappConfig',
]
```

### Step 6: Create Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## Deployment Checklist

- [ ] Change DEBUG to False
- [ ] Update ALLOWED_HOSTS
- [ ] Generate new SECRET_KEY
- [ ] Configure PostgreSQL
- [ ] Set up static files (WhiteNoise or CDN)
- [ ] Configure email backend
- [ ] Set up HTTPS
- [ ] Configure CORS
- [ ] Set up error logging
- [ ] Configure payment gateways
- [ ] Test all features
- [ ] Set up database backups

## Common Issues & Solutions

### Issue: Import Error
```bash
# Solution: Make sure app is in INSTALLED_APPS in settings.py
```

### Issue: Static Files Not Loading
```bash
# Solution: Run collectstatic
python manage.py collectstatic --noinput
```

### Issue: Database Locked
```bash
# Solution: Delete db.sqlite3 and run migrations
rm db.sqlite3
python manage.py migrate
```

### Issue: Port 8000 Already in Use
```bash
# Solution: Use different port
python manage.py runserver 8001
```

### Issue: Template Not Found
```bash
# Solution: Check TEMPLATES['DIRS'] in settings.py
# Ensure app is in INSTALLED_APPS
```

## Useful Code Snippets

### Check if User is Admin
```python
if user.is_staff or user.is_superuser:
    # User is admin
```

### Get User's Cart
```python
try:
    cart = request.user.cart
except Cart.DoesNotExist:
    cart = Cart.objects.create(user=request.user)
```

### Filter by Date Range
```python
from django.utils import timezone
from datetime import timedelta

last_30_days = timezone.now() - timedelta(days=30)
orders = Order.objects.filter(created_at__gte=last_30_days)
```

### Send Email
```python
from django.core.mail import send_mail

send_mail(
    'Subject',
    'Message body',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
```

### Aggregate Data
```python
from django.db.models import Sum, Count

total = Order.objects.aggregate(Sum('total_amount'))
count = Product.objects.aggregate(Count('id'))
```

## API Testing with cURL

```bash
# Test product endpoint
curl http://127.0.0.1:8000/products/

# Test search
curl "http://127.0.0.1:8000/search/?q=headphones"

# Test login (POST)
curl -X POST http://127.0.0.1:8000/accounts/login/ \
  -d "username=admin&password=password"
```

## Performance Optimization

### Enable Query Count Display
```python
# In settings.py for development
if DEBUG:
    MIDDLEWARE += ['django.middleware.cache.CacheMiddleware']
```

### Use Select Related for Foreign Keys
```python
products = Product.objects.select_related('category')
```

### Use Prefetch Related for Reverse ForeignKey
```python
products = Product.objects.prefetch_related('images')
```

### Add Indexes
```python
class Product(models.Model):
    name = models.CharField(max_length=300, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
```

## Useful Links

- Django Docs: https://docs.djangoproject.com/
- Django Models: https://docs.djangoproject.com/en/stable/topics/db/models/
- Bootstrap 5: https://getbootstrap.com/
- Font Awesome Icons: https://fontawesome.com/

---

**Pro Tips:**
- Always use migrations for database changes
- Use virtual environments for project isolation
- Test locally before deploying
- Keep SECRET_KEY secure
- Use environment variables for sensitive data
- Regular backups of database and media files
- Monitor error logs in production
