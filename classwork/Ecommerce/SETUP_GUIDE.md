# EzyMart - Professional eCommerce Platform

## Complete Setup and Installation Guide

This is a production-ready eCommerce application built with Django, featuring multiple apps, a comprehensive admin dashboard, and modern UI with Bootstrap 5.

---

## Table of Contents

1. [Project Structure](#project-structure)
2. [Installation](#installation)
3. [Database Setup](#database-setup)
4. [Running the Application](#running-the-application)
5. [Features Overview](#features-overview)
6. [Admin Panel](#admin-panel)
7. [Customization Guide](#customization-guide)
8. [Deployment](#deployment)

---

## Project Structure

```
ecommerce_project/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database (created after migrations)
│
├── ecommerce/               # Main project folder
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL routing
│   ├── wsgi.py              # WSGI application
│   └── asgi.py              # ASGI application
│
├── accounts/                # User authentication app
│   ├── models.py            # UserProfile model
│   ├── views.py             # Login, Register, Profile views
│   ├── forms.py             # User forms
│   ├── urls.py              # App URLs
│   └── admin.py             # Admin configuration
│
├── products/                # Product management app
│   ├── models.py            # Product, Category, ProductImage, Wishlist
│   ├── views.py             # Product list, detail, search views
│   ├── forms.py             # Product filter form
│   ├── urls.py              # App URLs
│   └── admin.py             # Admin configuration
│
├── orders/                  # Cart and order management app
│   ├── models.py            # Cart, CartItem, Order, OrderItem
│   ├── views.py             # Cart, checkout, order views
│   ├── forms.py             # Checkout form
│   ├── urls.py              # App URLs
│   └── admin.py             # Admin configuration
│
├── payments/                # Payment gateway integration
│   ├── models.py            # Payment, PaymentLog models
│   ├── views.py             # Payment views
│   ├── forms.py             # Payment form
│   ├── urls.py              # App URLs
│   └── admin.py             # Admin configuration
│
├── reviews/                 # Product reviews and ratings
│   ├── models.py            # Review model
│   ├── views.py             # Review views
│   ├── forms.py             # Review form
│   ├── urls.py              # App URLs
│   └── admin.py             # Admin configuration
│
├── admin_panel/             # Custom admin dashboard
│   ├── models.py            # No models
│   ├── views.py             # Dashboard, analytics views
│   ├── urls.py              # App URLs
│   └── admin.py             # Admin configuration
│
├── templates/               # HTML templates
│   ├── base.html            # Base template (extends to all)
│   ├── 404.html             # 404 error page
│   ├── 500.html             # 500 error page
│   ├── accounts/            # Account templates
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── profile.html
│   │   └── change_password.html
│   ├── products/            # Product templates
│   │   ├── home.html
│   │   ├── product_list.html
│   │   ├── product_detail.html
│   │   ├── category_products.html
│   │   ├── search_results.html
│   │   └── wishlist.html
│   ├── orders/              # Order templates
│   │   ├── cart.html
│   │   ├── checkout.html
│   │   ├── order_confirmation.html
│   │   ├── order_history.html
│   │   └── order_detail.html
│   ├── payments/            # Payment templates
│   │   ├── razorpay.html
│   │   └── stripe.html
│   ├── reviews/             # Review templates
│   │   ├── add_review.html
│   │   └── my_reviews.html
│   └── admin_panel/         # Admin templates
│       ├── dashboard.html
│       ├── manage_products.html
│       ├── manage_orders.html
│       ├── manage_users.html
│       ├── manage_reviews.html
│       └── manage_categories.html
│
├── static/                  # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
│
└── media/                   # User uploads (product images, avatars)
    └── products/
```

---

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual Environment (recommended)
- Git

### Step 1: Clone or Download the Project

```bash
cd d:\python\classwork\Ecommerce\ecommerce_project
```

### Step 2: Create Virtual Environment

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r ../requirements.txt
```

### Step 4: Configure Settings (Optional)

Edit `ecommerce/settings.py` for production:

```python
# Change these for production:
DEBUG = False  # Set to False in production
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']
SECRET_KEY = 'your-super-secret-key'

# Database (use PostgreSQL in production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecommerce_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## Database Setup

### Step 1: Create Migrations

```bash
python manage.py makemigrations
```

You should see output like:
```
Migrations for 'accounts':
  accounts/migrations/0001_initial.py
    - Create model UserProfile
Migrations for 'products':
  products/migrations/0001_initial.py
    - Create model Category
    - Create model Product
    - Create model ProductImage
    - Create model Wishlist
    - Create model WishlistItem
...
```

### Step 2: Apply Migrations

```bash
python manage.py migrate
```

This creates all database tables.

### Step 3: Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

You'll be prompted to enter:
- Username: (your choice, e.g., admin)
- Email: your-email@example.com
- Password: (create a strong password)

### Step 4: Load Sample Data (Optional)

Create a management command to load sample products:

```bash
python manage.py loaddata sample_data.json
```

Or manually add data through the Django admin.

---

## Running the Application

### Development Server

```bash
python manage.py runserver
```

Access the application at: `http://127.0.0.1:8000/`

### Admin Panel Access

1. Go to: `http://127.0.0.1:8000/admin/`
2. Login with superuser credentials
3. Manage products, orders, users, categories

### Access Different Sections

- **Home**: `http://127.0.0.1:8000/`
- **Products**: `http://127.0.0.1:8000/products/`
- **Cart**: `http://127.0.0.1:8000/orders/cart/`
- **Account**: `http://127.0.0.1:8000/accounts/profile/`
- **Django Admin**: `http://127.0.0.1:8000/admin/`
- **Admin Panel**: `http://127.0.0.1:8000/admin-panel/`

---

## Features Overview

### 1. Accounts Module
- User Registration with email validation
- Login/Logout functionality
- User Profile management
- Password change and reset
- Profile picture upload

### 2. Products Module
- Product listing with pagination
- Category-based filtering
- Search functionality
- Product detail page with multiple images
- Wishlist feature
- Product ratings and reviews

### 3. Orders Module
- Shopping cart with session management
- Add/remove/update cart items
- Checkout process
- Order confirmation
- Order history and tracking
- Order cancellation

### 4. Payments Module
- Multiple payment methods (Cash on Delivery, Razorpay, Stripe)
- Payment gateway integration
- Payment logs and transaction tracking
- Refund handling

### 5. Reviews Module
- Product reviews with ratings (1-5 stars)
- Review moderation (approve/reject)
- User ratings display on product page
- Review deletion

### 6. Admin Panel
- Custom dashboard with analytics
- Product management (CRUD operations)
- Order management and status updates
- User management
- Review moderation
- Category management
- Real-time statistics

---

## Admin Panel

### Accessing the Admin Panel

1. Login as admin at `http://127.0.0.1:8000/admin/`
2. Go to Admin Panel: `http://127.0.0.1:8000/admin-panel/`

### Dashboard Features

- **Total Statistics**: Orders, Revenue, Users, Products
- **30-Day Analytics**: Order count and revenue trends
- **Order Status Breakdown**: Pending, Confirmed, Shipped, Delivered
- **Recent Orders**: Last 5 orders
- **Quick Actions**: Links to manage products, orders, users, reviews

### Managing Products

1. Go to: `/admin-panel/products/`
2. **Search**: Find products by name or SKU
3. **Add Product**: Click Django admin link to add
4. **Edit**: Update product details
5. **Activate/Deactivate**: Toggle product visibility
6. **Delete**: Remove products

### Managing Orders

1. Go to: `/admin-panel/orders/`
2. **View Details**: See full order information
3. **Update Status**: Change order status (pending → confirmed → shipped → delivered)
4. **Track Order**: View order items and amounts

---

## Customization Guide

### Changing Colors and Branding

Edit `templates/base.html` CSS variables:

```css
:root {
    --primary-color: #FF9900;      /* Change to your brand color */
    --secondary-color: #146EB4;    /* Secondary color */
    --success-color: #198754;
    --danger-color: #DC3545;
}
```

### Modifying Email Templates

Update email backend in `ecommerce/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

### Setting Up Payment Gateways

#### Razorpay Integration

1. Get API keys from [Razorpay Dashboard](https://dashboard.razorpay.com/)
2. Update `ecommerce/settings.py`:

```python
RAZORPAY_KEY_ID = 'your-key-id'
RAZORPAY_KEY_SECRET = 'your-key-secret'
```

#### Stripe Integration

1. Get API keys from [Stripe Dashboard](https://dashboard.stripe.com/)
2. Update `ecommerce/settings.py`:

```python
STRIPE_PUBLIC_KEY = 'pk_test_your_public_key'
STRIPE_SECRET_KEY = 'sk_test_your_secret_key'
```

### Adding Custom Product Fields

Edit `products/models.py` and add fields to Product model:

```python
class Product(models.Model):
    # ... existing fields ...
    color = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=50, blank=True)
    material = models.CharField(max_length=100, blank=True)
```

Then run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Sample Data Setup

### Create Categories via Django Admin

1. Go to: `http://127.0.0.1:8000/admin/products/category/`
2. Click "Add Category"
3. Enter:
   - Name: Electronics
   - Slug: electronics
   - Click Save

### Add Sample Products

1. Go to: `http://127.0.0.1:8000/admin/products/product/`
2. Click "Add Product"
3. Fill in:
   - Name: "Wireless Headphones"
   - SKU: "PROD-001"
   - Category: Electronics
   - Price: 2999
   - Stock: 50
   - Description: "High-quality wireless headphones"
4. Click Save
5. Add images: Go to Product Images section

---

## Deployment

### Deployment Checklist

- [ ] Set `DEBUG = False`
- [ ] Update `ALLOWED_HOSTS`
- [ ] Generate new `SECRET_KEY`
- [ ] Set up PostgreSQL database
- [ ] Configure email backend
- [ ] Set up static files (WhiteNoise or CDN)
- [ ] Configure media file storage (S3 or local)
- [ ] Set up HTTPS/SSL
- [ ] Configure CORS headers if needed
- [ ] Set up error logging

### Deploy to Heroku

```bash
# Install Heroku CLI and login
heroku login

# Create new app
heroku create your-app-name

# Set environment variables
heroku config:set DJANGO_SECRET_KEY='your-secret-key'
heroku config:set DEBUG='False'

# Add PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser
```

### Deploy to AWS

Use AWS Elastic Beanstalk with RDS PostgreSQL database.

---

## Troubleshooting

### Problem: ModuleNotFoundError

**Solution**: Ensure virtual environment is activated and requirements are installed:
```bash
pip install -r requirements.txt
```

### Problem: Database locked error

**Solution**: Delete `db.sqlite3` and run migrations again:
```bash
rm db.sqlite3
python manage.py migrate
```

### Problem: Port 8000 already in use

**Solution**: Use a different port:
```bash
python manage.py runserver 8001
```

### Problem: Static files not loading

**Solution**: Collect static files:
```bash
python manage.py collectstatic --noinput
```

---

## Important Notes

1. **Security**: Never commit `SECRET_KEY` or credentials to version control
2. **Database**: Use PostgreSQL in production, not SQLite
3. **Media Files**: Use cloud storage (S3) in production
4. **Email**: Configure real SMTP server in production
5. **HTTPS**: Always use HTTPS in production

---

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.0/)
- [Django Best Practices](https://docs.djangoproject.com/en/stable/topics/db/models/)

---

## License

This project is provided as-is for educational purposes.

---

## Support and Contact

For questions or issues, refer to the Django documentation or create issues in your repository.

**Happy Coding! 🚀**
