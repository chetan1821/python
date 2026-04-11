from django.contrib import admin
from .models import Payment, PaymentLog


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'payment_method', 'status', 'created_at')
    list_filter = ('payment_method', 'status', 'created_at')
    search_fields = ('order__order_number', 'transaction_id')
    readonly_fields = ('transaction_id', 'created_at', 'updated_at')


@admin.register(PaymentLog)
class PaymentLogAdmin(admin.ModelAdmin):
    list_display = ('payment', 'action', 'created_at')
    list_filter = ('action', 'created_at')
    search_fields = ('payment__transaction_id',)
    readonly_fields = ('created_at',)
