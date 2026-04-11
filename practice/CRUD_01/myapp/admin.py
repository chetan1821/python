from django.contrib import admin
from myapp.models import *

# Register your models here.
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'dept')
admin.site.register(Employee,EmployerAdmin)

