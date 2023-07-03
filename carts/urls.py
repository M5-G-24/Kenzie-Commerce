from django.urls import path
from carts.views import CartAPIView, CartDetailAPIView


urlpatterns = [
    path("carts/<int:user_id>/", CartAPIView.as_view(), name="cart-create"),
    path("carts/<int:pk>/", CartDetailAPIView.as_view(), name="cart-detail"),
]
