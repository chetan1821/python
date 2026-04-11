# EzyMart - Professional eCommerce Platform

A complete, production-ready Django eCommerce application with modern UI, comprehensive admin dashboard, and multiple payment integration options.

## 🌟 Key Features

### User Features
✅ User registration and authentication
✅ Profile management with avatar upload
✅ Product browsing with search and filters
✅ Wishlist functionality
✅ Shopping cart with AJAX updates
✅ Secure checkout process
✅ Multiple payment options (COD, Razorpay, Stripe)
✅ Order tracking and history
✅ Product reviews and ratings
✅ Email notifications

### Admin Features
✅ Custom admin dashboard with analytics
✅ Product management (CRUD)
✅ Order management and tracking
✅ User management
✅ Review moderation
✅ Category management
✅ Real-time statistics and charts
✅ Sales analytics

### Technical Features
✅ Modular Django app architecture
✅ Clean separation of concerns
✅ Bootstrap 5 responsive design
✅ AJAX-enabled cart operations
✅ Database optimization with indexes
✅ Security best practices
✅ Payment gateway integration
✅ Image optimization and caching

## 📁 Project Structure

```
Ecommerce/
├── ecommerce_project/          # Django project
│   ├── ecommerce/              # Main project settings
│   ├── accounts/               # User authentication
│   ├── products/               # Product management
│   ├── orders/                 # Cart & orders
│   ├── payments/               # Payment processing
│   ├── reviews/                # Product reviews
│   ├── admin_panel/            # Admin dashboard
│   ├── templates/              # HTML templates
│   ├── static/                 # CSS, JS, images
│   ├── media/                  # User uploads
│   └── manage.py               # Django CLI
├── requirements.txt            # Python dependencies
├── SETUP_GUIDE.md             # Complete setup instructions
└── README.md                  # This file
```

## 🚀 Quick Start

### 1. Installation

```bash
cd ecommerce_project

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r ../requirements.txt
```

### 2. Database Setup

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser (admin account)
python manage.py createsuperuser
```

### 3. Run the Server

```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

## 🔗 Important URLs

| URL | Purpose |
|-----|---------|
| `/` | Home page |
| `/products/` | Product listing |
| `/accounts/register/` | User registration |
| `/accounts/login/` | User login |
| `/accounts/profile/` | User profile |
| `/orders/cart/` | Shopping cart |
| `/orders/checkout/` | Checkout |
| `/reviews/` | Product reviews |
| `/admin/` | Django admin |
| `/admin-panel/` | Custom admin dashboard |

## 📚 API Endpoints

### Products
- `GET /products/` - List all products
- `GET /product/<id>/` - Get product details
- `GET /search/?q=<query>` - Search products

### Orders
- `POST /add-to-cart/<id>/` - Add to cart
- `GET /orders/cart/` - View cart
- `POST /orders/checkout/` - Process checkout
- `GET /orders/` - Order history

### Account
- `POST /accounts/register/` - Register user
- `POST /accounts/login/` - Login user
- `GET /accounts/profile/` - User profile

## 🛠️ Customization

### Change Brand Colors

Edit `templates/base.html`:
```css
:root {
    --primary-color: #FF9900;
    --secondary-color: #146EB4;
}
```

### Add New App

```bash
python manage.py startapp new_app

# 1. Create models in new_app/models.py
# 2. Add app to INSTALLED_APPS in settings.py
# 3. Create migrations: python manage.py makemigrations
# 4. Apply migrations: python manage.py migrate
```

### Configure Payment Gateway

Edit `ecommerce/settings.py`:
```python
RAZORPAY_KEY_ID = 'your-key'
RAZORPAY_KEY_SECRET = 'your-secret'

STRIPE_PUBLIC_KEY = 'pk_test_...'
STRIPE_SECRET_KEY = 'sk_test_...'
```

## 📊 Database Models

### Accounts
- `UserProfile` - Extended user information

### Products
- `Category` - Product categories
- `Product` - Product details
- `ProductImage` - Multiple product images
- `Wishlist` - User wishlist
- `WishlistItem` - Wishlist items

### Orders
- `Cart` - Shopping cart
- `CartItem` - Items in cart
- `Order` - Customer orders
- `OrderItem` - Items in order

### Payments
- `Payment` - Payment records
- `PaymentLog` - Payment transaction logs

### Reviews
- `Review` - Product reviews and ratings

## 🔐 Security Features

- ✅ CSRF protection
- ✅ SQL injection prevention (ORM)
- ✅ XSS protection
- ✅ Secure password hashing
- ✅ Session security
- ✅ HTTPS recommended
- ✅ Input validation and sanitization

## 📈 Scalability

The application is designed for scalability:

- **Database**: PostgreSQL ready
- **Static Files**: CDN compatible
- **Media Files**: Cloud storage (S3) compatible
- **Caching**: Redis integration ready
- **Load Balancing**: Horizontally scalable
- **Microservices**: Modular app architecture

## 🧪 Testing

Run tests:
```bash
python manage.py test
```

## 📋 Tasks Checklist

Development:
- [x] User authentication system
- [x] Product management
- [x] Shopping cart
- [x] Order processing
- [x] Payment integration
- [x] Product reviews
- [x] Admin dashboard
- [x] Responsive design

Optional:
- [ ] Email notifications
- [ ] SMS notifications
- [ ] Inventory tracking
- [ ] Shipping integration
- [ ] Mobile app API
- [ ] Social login
- [ ] Analytics dashboard
- [ ] Recommendation engine

## 🐛 Known Limitations

1. Payment integration is in demo mode (requires API keys)
2. Email backend uses console (configure SMTP for production)
3. SQLite database suitable for development only
4. Static files serve through Django (use WhiteNoise for production)

## 📞 Support

For detailed setup instructions, see [SETUP_GUIDE.md](SETUP_GUIDE.md)

## 📄 License

This project is provided for educational purposes.

## 🎓 Learning Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Models](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django Views](https://docs.djangoproject.com/en/stable/topics/http/views/)
- [Django URL Dispatcher](https://docs.djangoproject.com/en/stable/topics/http/urls/)
- [Bootstrap 5](https://getbootstrap.com/)

---

**Built with ❤️ using Django** 🚀
