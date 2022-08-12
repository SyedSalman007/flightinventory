from rest_framework.views import APIView
from rest_framework import permissions
from flightinventory.flight.api.request_serializer import SearchingFlightSerializer
from rest_framework.response import Response
from rest_framework import status
from flightinventory.flight.models import Flight, Airport
from flightinventory.flight.api.serializer import FlightSerializer, AirportSerializers, AuthorizedFlightSerializer


# from rest_framework.authentication


class FlightSearchAPI(APIView):
    # authentication_classes =
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        print("Salman")

        flights = SearchingFlightSerializer(data=request.data, many=True)
        try:
            flights.is_valid(raise_exception=True)
            valid_flights = flights.validated_data
            print(valid_flights)
            flight_numbers = [val['flight_number'] for val in valid_flights]
            print(flight_numbers)
            flights_exist = Flight.objects.filter(flight_number__in=flight_numbers)
            # print(exist)
            return Response(
                data={
                    "message": "Flight exists in the database",
                    "user": FlightSerializer(flights_exist, many=True).data
                },
                status=status.HTTP_200_OK)
        except Exception as error:
            print(f"Error = {error}")
            return Response(data={"message": "Invalid data entered"}, status=status.HTTP_400_BAD_REQUEST)


class AuthorizedFlightSearchAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def SerializerChecker(self):
        if self.request.user.is_authenticated:
            return AuthorizedFlightSerializer
        else:
            return FlightSerializer

    def get(self, request):
        flights = SearchingFlightSerializer(data=request.data, many=True)
        try:
            flights.is_valid(raise_exception=True)
            valid_flights = flights.validated_data
            print(valid_flights)
            flight_numbers = [val['flight_number'] for val in valid_flights]
            print(flight_numbers)
            flights_exist = Flight.objects.filter(flight_number__in=flight_numbers)
            # print(exist)
            serializer = self.SerializerChecker()
            return Response(
                data={
                    "message": "Flight exists in the database",
                    "user": serializer(flights_exist, many=True).data
                },
                status=status.HTTP_200_OK)
        except Exception as error:
            print(f"Error = {error}")
            return Response(data={"message": "Invalid data entered"}, status=status.HTTP_400_BAD_REQUEST)
