"""
Serializers for recipe APIs
"""
from rest_framework import serializers
from core.models import RealEstate


class RealEstateSerializer(serializers.ModelSerializer):
    """Serializer for real estate."""

    class Meta:
        model = RealEstate
        fields = ['city', 'area', 'qt_rooms', 'qt_bathrooms', 'qt_parking_spaces', 'floor',
                  'allows_animals', 'furnished', 'vl_hoa', 'vl_rent', 'vl_tax', 'vl_fire_insurance']
