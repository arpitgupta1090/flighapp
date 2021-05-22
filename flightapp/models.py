from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.


class Flight(models.Model):
    flightNumber = models.CharField(max_length=10)
    Airline = models.CharField(max_length=50)
    departureCity = models.CharField(max_length=50)
    arrivalCity = models.CharField(max_length=50)
    dateOfDeparture = models.DateField()
    timeOfDeparture = models.TimeField()

    def __str__(self):
        return f"{self.flightNumber}:{self.Airline}"


class Passenger(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    middleName = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.firstName}_{self.lastName}"


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
