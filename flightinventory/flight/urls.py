from django.urls import path
from flightinventory.flight.api.views import FlightSearchAPI, AuthorizedFlightSearchAPI

urlpatterns = [
    path("search/", FlightSearchAPI.as_view(), name="flight_search"),
    path("auth/search", AuthorizedFlightSearchAPI.as_view(), name="auth_flight_search")
]
