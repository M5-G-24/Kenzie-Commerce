from django.urls import path

from . import views

urlpatterns = [
    path("orders/<int:user_id>/", views.OrderListCreateView.as_view()),
    # path("orders/<int:pk>/", views.OrderCreateUpdateDestroyDetailsView.as_view()),
]
