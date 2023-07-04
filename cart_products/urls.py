from django.urls import path
from .views import CartProductView, CartProductDetailView

urlpatterns = [
    path('cart/<int:cart_id>/cart-products/', CartProductView.as_view(), name='cart-products'),
    path('cart/<int:cart_id>/cart-products/<int:pk>/', CartProductDetailView.as_view(), name='cart-product-detail'),
]