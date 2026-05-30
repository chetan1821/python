from django.urls import path,include
from myapp.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('categories', CategoryViewset)
router.register('products', ProductViewset)

urlpatterns = [
    path('', include(router.urls)),
]