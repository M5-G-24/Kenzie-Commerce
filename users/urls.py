from django.urls import path
from .views import UserCreateAPIView, UserListAPIView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("users/", UserCreateAPIView.as_view()),
    path("user/", UserDetailView.as_view()),
    path("get/users/", UserListAPIView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
]
