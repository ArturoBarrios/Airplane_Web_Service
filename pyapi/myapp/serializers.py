from .models import *
from rest_framework import serializers

class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ('airplane_id', 'manufacturer', 'max_seats', 'type')

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ('airport_id', 'airport_name', 'city', 'state')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('cust_id', 'c_first_name', 'c_last_name', 'address', 'city', 'postal_code', 'email', 'phone')

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ('flight_id', 'scheduled_dep_time', 'scheduled_arriv_time', 'departure_airportid', 'arrival_airportid')
