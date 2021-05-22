from rest_framework import serializers
from flightapp.models import Flight, Passenger, Reservation
import re


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def validate_flightNumber(self, flight_number):
        if not re.match('^[a-zA-Z0-9]+$', flight_number) :
            raise serializers.ValidationError("Flight number should be alphanumeric")
        return flight_number


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

    def validate(self, data):
        if len(data['phone']) > 10:
            raise serializers.ValidationError("Phone number can't be greater than 10 digits")
        if not re.match('[a-zA-Z0-9._-]+@[\d\w]+.\w', data['email']):
            raise serializers.ValidationError("Invalid email id")
        return data


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
