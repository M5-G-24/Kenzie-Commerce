from django.urls import path

from carts.views import CartListCreateView, CartDetailAPIView


urlpatterns = [
    path("carts/", CartListCreateView.as_view(), name="cart-create"),

    path("carts/<int:pk>/", CartDetailAPIView.as_view(), name="cart-detail"),
]
