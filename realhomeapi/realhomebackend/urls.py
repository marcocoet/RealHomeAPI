from django.urls import path
from realhomebackend.views import RealEstateTypeListAPIView, Realestate_All_BuyAPIView
from realhomebackend.views import PropertiesListCreateAPIView, PropertiesDetailAPIView, GeocodeAPIView

urlpatterns = [
    path('realestatetype/list/', RealEstateTypeListAPIView.as_view()),
    path('properties/list/', Realestate_All_BuyAPIView.as_view()),

    # Property API endpoints
    path('properties/', PropertiesListCreateAPIView.as_view(), name='properties-list'),
    path('properties/<int:pk>/', PropertiesDetailAPIView.as_view(), name='property-detail'),

    # Geocoding API endpoint
    path('geocode/<str:address>/', GeocodeAPIView.as_view(), name='geocode'),
]
