from django.urls import path
from .views import UserListCreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("users/", UserListCreateAPIView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
]
