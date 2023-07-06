from django.shortcuts import render
from .models import Order
from .serializer import OrderSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from cart_products.models import CartProduct
from rest_framework.views import Request, Response, status


class OrderListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, user_id):
        cart_products = CartProduct.objects.filter(user_id=user_id)

        orders = []

        for product in cart_products:
            print("product: ", product.total)
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
    # permission_classes = [IsAdminUser]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
