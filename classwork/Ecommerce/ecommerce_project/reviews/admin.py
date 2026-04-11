from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'is_approved', 'created_at')
    list_filter = ('rating', 'is_approved', 'created_at')
    search_fields = ('product__name', 'user__username', 'title')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Product & User', {
            'fields': ('product', 'user')
        }),
        ('Review Content', {
            'fields': ('title', 'comment', 'rating')
        }),
        ('Status', {
            'fields': ('is_approved',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
