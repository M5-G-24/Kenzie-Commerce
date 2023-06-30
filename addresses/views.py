from django.shortcuts import render
from rest_framework import generics
from .models import Address
from .serializer import AddressSerializer


class AddressCreateView(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressRetrieveUpdateDestroyDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
