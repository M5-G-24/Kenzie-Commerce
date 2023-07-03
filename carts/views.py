from .serializers import CartSerializer
from rest_framework import generics
from .models import Cart


class CartAPIView(generics.CreateAPIView):
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
