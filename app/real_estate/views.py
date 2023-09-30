from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiResponse,
)

from real_estate import serializers


class RealEstatePredictionView(APIView):
    """Endpoint for real estate prediction"""
    # serializer_class = serializers.RealEstateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=serializers.RealEstateSerializer,
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description="Prediction result",
                examples=[
                    1
                ]
            )
        },
    )
    def post(self, request):
        # Lógica para calcular a predição
        prediction_data = {}
        return Response(prediction_data, status=status.HTTP_200_OK)
