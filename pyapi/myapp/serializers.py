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
