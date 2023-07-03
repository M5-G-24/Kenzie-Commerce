from django.urls import path
from .views import AddressListView, AddressCreateDetailsView


urlpatterns = [
    path("addresses/", AddressListView.as_view()),
    path("addresses/<int:pk>/", AddressCreateDetailsView.as_view()),
]
