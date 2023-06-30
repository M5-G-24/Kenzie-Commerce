from django.urls import path
from products.views import ProductListAPIView, ProductDetailView

urlpatterns = [
    # /products/: Rota para listar os produtos e permitir a filtragem por nome, categoria e ID.
    path("products/", ProductListAPIView.as_view(), name="product-list"),
    # /products/<int:pk>/: Rota para obter os detalhes de um produto específico com base no ID.
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
]
