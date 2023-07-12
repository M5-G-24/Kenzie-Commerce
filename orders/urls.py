from django.urls import path

from . import views

urlpatterns = [
    path("orders/", views.OrderListUserCreateView.as_view()),
    path("orders/seller/", views.OrderListSellerView.as_view()),
    path("orders/<int:pk>/", views.OrderDetailsView.as_view()),
]
