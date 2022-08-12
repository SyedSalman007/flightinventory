from rest_framework import serializers


class SearchingFlightSerializer(serializers.Serializer):
    flight_number = serializers.CharField()
