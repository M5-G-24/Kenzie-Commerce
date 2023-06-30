from django.urls import path
from . import views


urlpatterns = [
    path("addresses/", views.AddressCreateView.as_view()),
    path(
        "addresses/<int:pk>/", views.AddressRetrieveUpdateDestroyDetailsView.as_view()
    ),
]
