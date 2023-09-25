# uavlists/api/serializers.py
from rest_framework import serializers
from uav_management.models import UAV

class UavListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UAV
        fields = '__all__'
