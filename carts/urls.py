from django.urls import path
from carts.views import CartCreateAPIView, CartDetailAPIView


urlpatterns = [
    # /carts/: Rota para criar um novo carrinho com os produtos selecionados
    ## antes de finalizar a compra.
    path("carts/<int:user_id>/", CartCreateAPIView.as_view(), name="cart-create"),
    # /carts/<int:pk>/: Rota para obter os detalhes de um carrinho específico
    ## com base no ID e também excluir um carrinho existente.
    path("carts/<int:pk>/", CartDetailAPIView.as_view(), name="cart-detail"),
]
