from django.contrib import admin
from CRUD_APP.models import *
# Register your models here.
class PeopleAdmin(admin.ModelAdmin):
    list_display=('name','age','phone','image')
admin.site.register(People,PeopleAdmin)
# user=>data password=>data
