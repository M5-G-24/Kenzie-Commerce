from django.urls import path
from .views import AddressListView, AddressCreateView, AddressDetailsView


urlpatterns = [
    path("addresses/", AddressListView.as_view()),
    path("get/addresses/", AddressCreateView.as_view()),
    path("addresses/create/", AddressDetailsView.as_view()),
]
