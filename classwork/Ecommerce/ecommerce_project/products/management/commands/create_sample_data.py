from django.core.management.base import BaseCommand
from products.models import Category, Product
from decimal import Decimal
import random

class Command(BaseCommand):
    help = 'Populate database with 20 random products for preview'
    
    def handle(self, *args, **options):
        # Sample categories
        categories_data = [
            {'name': 'Electronics', 'slug': 'electronics', 'description': 'Electronic gadgets and devices'},
            {'name': 'Fashion', 'slug': 'fashion', 'description': 'Clothing and accessories'},
            {'name': 'Books', 'slug': 'books', 'description': 'Books and reading materials'},
            {'name': 'Home & Living', 'slug': 'home-living', 'description': 'Home and kitchen items'},
        ]
        
        # Create categories
        categories = []
        for cat_data in categories_data:
            cat, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={
                    'name': cat_data['name'],
                    'description': cat_data['description'],
                    'is_active': True
                }
            )
            categories.append(cat)
            if created:
                self.stdout.write(f'Created category: {cat.name}')
        
        # Sample product data
        products_data = [
            # Electronics
            {'name': 'iPhone 15 Pro', 'category': 0, 'price': 79999, 'discount': 74999},
            {'name': 'Samsung Galaxy S24', 'category': 0, 'price': 69999, 'discount': 64999},
            {'name': 'MacBook Air M3', 'category': 0, 'price': 119999, 'discount': 109999},
            {'name': 'Sony WH-1000XM5 Headphones', 'category': 0, 'price': 29999, 'discount': 24999},
            {'name': 'iPad Pro 12.9', 'category': 0, 'price': 89999, 'discount': 79999},
            
            # Fashion
            {'name': 'Nike Air Max 90', 'category': 1, 'price': 8999, 'discount': 6999},
            {'name': 'Adidas Ultraboost', 'category': 1, 'price': 12999, 'discount': 9999},
            {'name': 'Levi\'s 501 Jeans', 'category': 1, 'price': 4999, 'discount': 3999},
            {'name': 'Puma Black T-Shirt', 'category': 1, 'price': 1999, 'discount': 1299},
            {'name': 'Calvin Klein Watch', 'category': 1, 'price': 15999, 'discount': 12999},
            
            # Books
            {'name': 'Atomic Habits', 'category': 2, 'price': 599, 'discount': 399},
            {'name': 'The Power of Now', 'category': 2, 'price': 699, 'discount': 499},
            {'name': 'Rich Dad Poor Dad', 'category': 2, 'price': 549, 'discount': 349},
            {'name': 'Think and Grow Rich', 'category': 2, 'price': 599, 'discount': 399},
            {'name': 'The Art of War', 'category': 2, 'price': 299, 'discount': 199},
            
            # Home & Living
            {'name': 'Stainless Steel Cookware Set', 'category': 3, 'price': 4999, 'discount': 3499},
            {'name': 'Bamboo Cutting Board Set', 'category': 3, 'price': 1299, 'discount': 899},
            {'name': 'LED Table Lamp', 'category': 3, 'price': 2999, 'discount': 1999},
            {'name': 'Cotton Bed Sheet Set', 'category': 3, 'price': 3999, 'discount': 2999},
            {'name': 'Kitchen Knife Set', 'category': 3, 'price': 2499, 'discount': 1799},
        ]
        
        # Create products
        created_count = 0
        for i, prod_data in enumerate(products_data, 1):
            product, created = Product.objects.get_or_create(
                sku=f'DEMO-{i:03d}',
                defaults={
                    'name': prod_data['name'],
                    'category': categories[prod_data['category']],
                    'description': f'High-quality {prod_data["name"].lower()} with excellent features',
                    'long_description': f'This is a premium {prod_data["name"]} product with the best quality. Perfect for everyday use and provides great value for money.',
                    'price': Decimal(str(prod_data['price'])),
                    'discount_price': Decimal(str(prod_data['discount'])),
                    'stock': random.randint(5, 50),
                    'is_active': True,
                    'is_featured': random.choice([True, False])
                }
            )
            if created:
                created_count += 1
                badge = '[FEATURED]' if product.is_featured else '[REGULAR]'
                self.stdout.write(f'{badge} Created: {product.name} - Rs.{product.price} -> Rs.{product.discount_price}')
        
        total_products = Product.objects.count()
        self.stdout.write(self.style.SUCCESS(f'\n==== Added {created_count} new products! Total: {total_products} products ==== '))
