from rest_framework import serializers
from flightinventory.flight.models import Flight, Airport


class AirportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = "__all__"


class OriginAirportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = [
            "iata"
        ]


class FlightSerializer(serializers.ModelSerializer):
    origin = OriginAirportSerializers()
    destination = OriginAirportSerializers()

    class Meta:
        model = Flight
        fields = [
            "origin",
            "destination",
            "departure_time",
            "arrival_time",
        ]


class AuthorizedFlightSerializer(serializers.ModelSerializer):
    origin = OriginAirportSerializers()
    destination = OriginAirportSerializers()

    class Meta:
        model = Flight
        fields = [
            "origin",
            "destination",
            "departure_time",
            "arrival_time",
            "base_fare",
            "tax",
        ]




