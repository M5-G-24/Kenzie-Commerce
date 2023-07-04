from rest_framework import generics
from .models import CartProduct
from .serializers import CartProductSerializer, CartProductUpdateSerializer


class CartProductView(generics.ListCreateAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

    def perform_create(self, serializer):
        serializer.save(cart=self.request.cart, product=self.request.product)


class CartProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductUpdateSerializer
