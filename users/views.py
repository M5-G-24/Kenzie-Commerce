from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class UserView(generics.CreateAPIView):
     queryset = User.objects.all()
     serializer_class = UserSerializer
     
     def perform_create(self, serializer):
          if self.request.data['role'] == "Seller":
               serializer.save(is_staff = True)