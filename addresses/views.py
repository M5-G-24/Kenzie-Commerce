from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Address
from .serializer import AddressSerializer
from users.models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsOwnerOnly


class AddressListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser | IsOwnerOnly]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        user = get_object_or_404(User, pk=pk)
        serializer.save(user=user)
