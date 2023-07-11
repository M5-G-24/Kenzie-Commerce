from django.urls import path
from .views import CartProductView, CartProductDetailView

urlpatterns = [
    path(
        "cart_products/",
        CartProductView.as_view(),
        name="cart-products",
    ),
    path(
        "cart_products/cart-products/<int:pk>/",
        CartProductDetailView.as_view(),
        name="cart-product-detail",
    ),
]
