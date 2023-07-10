from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class ProductListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get("name")
        category = self.request.query_params.get("category")
        id = self.request.query_params.get("id")

        if name:
            queryset = queryset.filter(name__icontains=name)
        if category:
            queryset = queryset.filter(category=category)
        if id:
            queryset = queryset.filter(id=id)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
