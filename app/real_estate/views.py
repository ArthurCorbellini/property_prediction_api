from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from real_estate import serializers
import neural_model.model as neural_model


class RealEstatePredictionView(APIView):
    """Endpoint for real estate prediction"""
    serializer_class = serializers.RealEstateSerializer
    # authentication_classes = TokenAuthentication
    # permission_classes = IsAuthenticated

    def post(self, request):
        obj = serializers.RealEstateSerializer(data=request.data)

        # data = {
        #     "city": "São Paulo",
        #     "area": 70,
        #     "rooms": 2,
        #     "bathroom": 1,
        #     "parking_spaces": 1,
        #     "animal": "acept",
        #     "furniture": "furnished",
        #     "hoa": 2065,
        #     "rent": 3300,
        #     "property_tax": 211,
        #     "fire_insurance": 42,
        # }

        if not obj.is_valid():
            return Response(obj.errors, status=status.HTTP_400_BAD_REQUEST)

        prediction_data = neural_model.predict(obj.data)

        return Response(prediction_data, status=status.HTTP_200_OK)
