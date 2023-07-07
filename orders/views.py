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

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)

    def post(self, request):
        user = request.user
        cart_products = CartProduct.objects.filter(user_id=user)

        orders = []
        insufficient_stock_products = []

        for product in cart_products:
            print("product.product.stock: ", product.product.stock)
            if product.amount > product.product.stock:
                insufficient_stock_products.append(product)
                continue

            order_dict = {
                "user_id": product.user_id,
                "product_id": product.product_id,
                "amount": product.amount,
                "total": product.total,
                "status": "placed",
            }

            order = Order.objects.create(**order_dict)
            orders.append(order)

            product.product.stock -= product.amount
            product.product.save()

        if insufficient_stock_products:
            product_info = []
            for product in insufficient_stock_products:
                product_name = product.product.name
                available_quantity = product.product.stock
                product_info.append(
                    f"{product_name} (disponível: {available_quantity})"
                )

            error_message = "Os seguintes produtos não estão disponíveis na quantidade solicitada: {}".format(
                ", ".join(product_info)
            )

            return Response(
                {"error": error_message},
                status=status.HTTP_400_BAD_REQUEST,
            )

        cart_products.delete()

        serializer = OrderSerializer(instance=orders, many=True)
        serialized_data = serializer.data

        return Response(data=serialized_data, status=status.HTTP_201_CREATED)


class OrderDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOnly]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
