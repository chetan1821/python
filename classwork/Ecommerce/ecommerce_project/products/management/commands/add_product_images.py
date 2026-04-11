from django.core.management.base import BaseCommand
from products.models import Product, ProductImage
from django.core.files.base import ContentFile
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import random

class Command(BaseCommand):
    help = 'Add sample images to all products'
    
    def handle(self, *args, **options):
        products = Product.objects.all()
        colors = [
            (255, 107, 107),  # Red
            (74, 144, 226),   # Blue
            (76, 175, 80),    # Green
            (255, 193, 7),    # Yellow
            (156, 39, 176),   # Purple
            (233, 30, 99),    # Pink
            (0, 188, 212),    # Cyan
            (255, 152, 0),    # Orange
            (63, 81, 181),    # Indigo
            (244, 67, 54),    # Deep Red
        ]
        
        added_count = 0
        for product in products:
            # Check if product already has images
            if product.images.exists():
                self.stdout.write(f'SKIP: {product.name} (already has images)')
                continue
            
            # Create a colored image with product name
            color = random.choice(colors)
            img = Image.new('RGB', (500, 500), color=color)
            draw = ImageDraw.Draw(img)
            
            # Add text to image
            text = product.name[:20]  # Truncate long names
            try:
                # Try to use default font
                draw.text((250, 250), text, fill=(255, 255, 255), anchor="mm")
            except:
                # Fallback if font not available
                draw.text((250, 250), text, fill=(255, 255, 255))
            
            # Save image to BytesIO
            img_io = BytesIO()
            img.save(img_io, format='PNG')
            img_io.seek(0)
            
            # Create ProductImage
            image_name = f'{product.sku.lower()}.png'
            product_image = ProductImage.objects.create(
                product=product,
                image=ContentFile(img_io.read(), name=image_name),
                alt_text=product.name,
                is_primary=True
            )
            
            added_count += 1
            self.stdout.write(f'ADDED: Image for {product.name}')
        
        self.stdout.write(self.style.SUCCESS(f'\n==== Added {added_count} images! ===='))
