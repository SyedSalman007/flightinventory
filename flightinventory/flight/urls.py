from django.urls import path
from flightinventory.flight.api.views import FlightSearchAPI, AuthorizedFlightSearchAPI

urlpatterns = [
    path("search/", AuthorizedFlightSearchAPI.as_view(), name="flight_search"),
    path("auth_search", FlightSearchAPI.as_view(), name="auth_flight_search")
]
