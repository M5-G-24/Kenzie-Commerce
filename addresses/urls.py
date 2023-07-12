from django.urls import path
from .views import AddressListView, AddressCreateView, AddressDetailsView


urlpatterns = [
    path("addresses/", AddressListView.as_view()),
    path("addresses/create/", AddressCreateView.as_view()),
    path("addresses/<int:pk>/", AddressDetailsView.as_view()),
]
