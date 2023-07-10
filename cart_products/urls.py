from django.urls import path
from .views import CartProductView, CartProductDetailView

urlpatterns = [
    path(
        "cart_products/<int:user_id>/",
        CartProductView.as_view(),
        name="cart-products",
    ),
    path(
        "cart_products/<int:user_id>/cart-products/<int:pk>/",
        CartProductDetailView.as_view(),
        name="cart-product-detail",
    ),
]
