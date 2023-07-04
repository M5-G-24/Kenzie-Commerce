from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Address
from .serializer import AddressSerializer
from users.models import User


class AddressListView(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressCreateDetailsView(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        user = get_object_or_404(User, pk=pk)
        serializer.save(user=user)
