from dataclasses import field
from statistics import mode

from rest_framework import serializers
from MyApps.logistics.models import Transport, Route, Service

class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = "__all__"

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

# class RouteTransportSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RouteTransport
#         fields = "__all__"
       