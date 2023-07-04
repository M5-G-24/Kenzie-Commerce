from rest_framework import generics
from .models import CartProduct
from .serializers import CartProductSerializer, CartProductUpdateSerializer
from carts.models import Cart
from products.models import Product

class CartProductView(generics.ListCreateAPIView):
    serializer_class = CartProductSerializer

    def get_queryset(self):
        cart_id = self.kwargs['cart_id']
        return CartProduct.objects.filter(cart_id=cart_id)

    def perform_create(self, serializer):
        cart_id = self.kwargs['cart_id']
        cart = Cart.objects.get(id=cart_id)

        product_id = self.request.data.get('product')
        product = Product.objects.get(id=product_id)

        serializer.save(cart=cart, product=product)


class CartProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartProductUpdateSerializer

    def get_queryset(self):
        cart_id = self.kwargs['cart_id']
        return CartProduct.objects.filter(cart_id=cart_id)

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs['pk']
        obj = generics.get_object_or_404(queryset, pk=pk)
        return obj
