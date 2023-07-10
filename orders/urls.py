from django.urls import path

from . import views

urlpatterns = [
    path("orders/", views.OrderListCreateView.as_view()),
    path("orders/<int:pk>/", views.OrderDetailsView.as_view()),
]
