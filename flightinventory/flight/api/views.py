from rest_framework.views import APIView
from rest_framework import permissions
from flightinventory.flight.api.request_serializer import SearchingFlightSerializer
from rest_framework.response import Response
from rest_framework import status
from flightinventory.flight.models import Flight
from flightinventory.flight.api.serializer import FlightSerializer, AuthorizedFlightSerializer
import logging


class AuthorizedFlightSearchAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        logging.info("Text")

        flights = SearchingFlightSerializer(data=request.data, many=True)
        try:
            flights.is_valid(raise_exception=True)
            valid_flights = flights.validated_data
            logging.info(valid_flights)
            flight_numbers = [val['flight_number'] for val in valid_flights]
            logging.info(flight_numbers)
            flights_exist = Flight.objects.filter(flight_number__in=flight_numbers)
            return Response(
                data={
                    "message": "Flight exists in the database",
                    "user": FlightSerializer(flights_exist, many=True).data
                },
                status=status.HTTP_200_OK)
        except Exception as error:
            logging.exception(f"Error = {error}")
            return Response(data={"message": "Invalid data entered"}, status=status.HTTP_400_BAD_REQUEST)


class FlightSearchAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get_serializer(self):
        return AuthorizedFlightSerializer if self.request.user.is_authenticated else FlightSerializer

    def get(self, request):
        flights = SearchingFlightSerializer(data=request.data, many=True)
        try:
            flights.is_valid(raise_exception=True)
            valid_flights = flights.validated_data
            logging.info(valid_flights)
            flight_numbers = [val['flight_number'] for val in valid_flights]
            logging.info(flight_numbers)
            flights_exist = Flight.objects.filter(flight_number__in=flight_numbers)
            serializer = self.get_serializer()
            return Response(
                data={
                    "message": "Flight exists in the database",
                    "user": serializer(flights_exist, many=True).data
                },
                status=status.HTTP_200_OK)
        except Exception as error:
            logging.exception(f"Error = {error}")
            return Response(data={"message": "Invalid data entered"}, status=status.HTTP_400_BAD_REQUEST)
