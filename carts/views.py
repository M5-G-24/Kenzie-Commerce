from django.shortcuts import render
from rest_framework import generics


from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer
from products.serializers import ProductSerializer
from products.models import Product


from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer
from products.models import Product


class CartCreateAPIView(APIView):
    def post(self, request, user_id):
        data = request.data
        product_ids = data.get("product_ids", [])

        # Verifica se os produtos existem e têm estoque disponível
        unavailable_products = []
        for product_id in product_ids:
            try:
                product = Product.objects.get(id=product_id)
                if product.stock == 0:
                    unavailable_products.append(product)
            except Product.DoesNotExist:
                pass

        if unavailable_products:
            serializer = CartSerializer(unavailable_products, many=True)
            return Response(
                {
                    "error": "Product(s) are unavailable",
                    "unavailable_products": serializer.data,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Cria o carrinho com os produtos selecionados e o user_id fornecido
        cart = Cart.objects.create(user_id=user_id)
        cart.products.add(*product_ids)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartDetailAPIView(APIView):
    def get(self, request, pk):
        cart = Cart.objects.get(pk=pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def delete(self, request, pk):
        cart = Cart.objects.get(pk=pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
