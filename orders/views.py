from .models import Order
from .serializer import OrderSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from cart_products.models import CartProduct
from rest_framework.views import Request, Response, status
from users.permissions import IsOwnerOnly

class OrderListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOnly]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, user_id):
        cart_products = CartProduct.objects.filter(user_id=user_id)
        print("cart_products: ", cart_products)

        orders = []

        for product in cart_products:
            order_dict = {
                "user_id": product.user_id,
                "product_id": product.product_id,
                "amount": product.amount,
                "total": product.total,
                "status": "placed",
            }

            order = Order.objects.create(**order_dict)
            orders.append(order)

        serializer = OrderSerializer(instance=orders, many=True)
        serialized_data = serializer.data

        return Response(data=serialized_data, status=status.HTTP_201_CREATED)


class OrderCreateUpdateDestroyDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOnly]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
