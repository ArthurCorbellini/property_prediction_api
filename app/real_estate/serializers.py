"""
Serializers for recipe APIs
"""
from rest_framework import serializers
from core.models import RealEstate


class RealEstateSerializer(serializers.ModelSerializer):
    """Serializer for real estate."""

    class Meta:
        model = RealEstate
        fields = [
            'city',
            'area',
            'rooms',
            'bathroom',
            'parking_spaces',
            'animal',
            'furniture',
            'hoa',
            'property_tax',
            'fire_insurance',
        ]
