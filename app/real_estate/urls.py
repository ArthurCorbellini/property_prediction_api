"""
URL mappings for the real_estate app.
"""
from django.urls import path
from real_estate import views


app_name = 'real_estate'

urlpatterns = [
    path('prediction/', views.RealEstatePredictionView.as_view(), name='prediction'),
]
