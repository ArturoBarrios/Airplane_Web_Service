from .models import Airplane
from rest_framework import serializers

class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ('airplane_id', 'manufacturer', 'max_seats', 'type')
