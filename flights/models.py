from django.conf import settings
from django.db import models

from user.models import User


class Crew(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Airport(models.Model):
    name = models.CharField(max_length=255)
    closest_big_city = models.CharField(max_length=255)


class AirplaneType(models.Model):
    name = models.CharField(max_length=255)


class Airplane(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()
    airplane_type = models.ForeignKey(
        AirplaneType, on_delete=models.CASCADE,
        related_name="airplanes"
        )


class Route(models.Model):
    source = models.ForeignKey(
        Airport, on_delete=models.CASCADE,
        related_name="source_routes"
    )
    destination = models.ForeignKey(
        Airport, on_delete=models.CASCADE,
        related_name="destination_routes"
    )
    distance = models.IntegerField()


class Flight(models.Model):
    route = models.ForeignKey(
        Route, on_delete=models.CASCADE,
        related_name="flights"
    )
    airplane = models.ForeignKey(
        Airplane, on_delete=models.CASCADE,
        related_name="flights"
    )
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    crew = models.ManyToManyField(Crew, blank=True)


class Order(models.Model):
    created_at = models.DateTimeField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    flight = models.ForeignKey(
        Flight, on_delete=models.CASCADE,
        related_name="tickets"
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE,
        related_name="tickets"
    )
