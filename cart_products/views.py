from .serializers import CartProductSerializer, CartProductUpdateSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsOwnerOnly
from products.models import Product
from rest_framework import generics
from .models import CartProduct
from users.models import User


class CartProductView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOnly]

    serializer_class = CartProductSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return CartProduct.objects.filter(user_id=user_id)

    def perform_create(self, serializer):
        amount = self.request.data.get("amount")
        user_id = self.request.user.id
        user = User.objects.get(id=user_id)

        product_id = self.request.data.get("product")
        product = Product.objects.get(id=product_id)

        total = product.price * amount

        serializer.save(user=user, product=product, total=total)


class CartProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOnly]

    serializer_class = CartProductUpdateSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return CartProduct.objects.filter(user_id=user_id)

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs["pk"]
        obj = generics.get_object_or_404(queryset, pk=pk)
        return obj
