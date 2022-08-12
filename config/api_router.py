from django.urls import path, include

urlpatterns = [
    path("", include("flightinventory.users.urls")),
    path("flights/", include("flightinventory.flight.urls")),
]
