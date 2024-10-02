from django.urls import path
from realhomebackend.views import RealEstateTypeListAPIView
from realhomebackend.views import PropertiesAPIView


urlpatterns = [
    path('realestatetype/list/', RealEstateTypeListAPIView.as_view()),
    path('properties/list', PropertiesAPIView.as_view()),
]
