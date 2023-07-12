from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Address
from .serializer import AddressSerializer
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

    def perform_create(self, serializer):
        user_id = self.request.user.id
        serializer.save(user_id=user_id)


class AddressDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser | IsOwnerOnly]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_object(self):
        user = self.request.user
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(self.queryset, user=user, pk=pk)
        return obj
