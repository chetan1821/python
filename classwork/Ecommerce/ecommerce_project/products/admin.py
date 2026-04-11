from django.contrib import admin
from .models import Category, Product, ProductImage, Wishlist, WishlistItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'is_active', 'created_at')
    list_filter = ('category', 'is_active', 'created_at')
    search_fields = ('name', 'description', 'sku')
    readonly_fields = ('created_at', 'updated_at', 'average_rating')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'sku', 'category', 'description')
        }),
        ('Pricing & Stock', {
            'fields': ('price', 'discount_price', 'stock')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'is_primary', 'created_at')
    list_filter = ('product', 'is_primary')
    search_fields = ('product__name',)


class WishlistItemInline(admin.TabularInline):
    model = WishlistItem
    extra = 1


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'item_count')
    list_filter = ('created_at',)
    search_fields = ('user__username',)
    inlines = [WishlistItemInline]
    readonly_fields = ('created_at', 'updated_at')
    
    def item_count(self, obj):
        """Display number of items in wishlist."""
        return obj.items.count()
    item_count.short_description = 'Items'


@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('wishlist', 'product', 'added_at')
    list_filter = ('added_at',)
    search_fields = ('wishlist__user__username', 'product__name')
