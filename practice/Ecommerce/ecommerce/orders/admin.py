from django.contrib import admin
from orders.models import *
# Register your models here.
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(OrderItem)