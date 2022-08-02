from django.db import models
from flightinventory.users.models import User


class Airport(models.Model):
    iata = models.CharField(max_length=3)
    city = models.CharField(max_length=50)


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="origin_airport")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="destination_airport")
    flight_number = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    base_fare = models.IntegerField()
    tax = models.IntegerField()
