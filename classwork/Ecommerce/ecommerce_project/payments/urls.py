from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('initiate/<int:order_id>/', views.initiate_payment, name='initiate_payment'),
    path('razorpay/<int:payment_id>/', views.razorpay_payment, name='razorpay_payment'),
    path('razorpay/callback/', views.razorpay_callback, name='razorpay_callback'),
    path('stripe/<int:payment_id>/', views.stripe_payment, name='stripe_payment'),
    path('success/<int:payment_id>/', views.payment_success, name='payment_success'),
    path('failure/<int:payment_id>/', views.payment_failure, name='payment_failure'),
]
