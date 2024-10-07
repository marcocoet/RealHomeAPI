from django.urls import path
from realhomebackend.views import RealEstateTypeListAPIView
from realhomebackend.views import Realestate_All_BuyAPIView


urlpatterns = [
    path('realestatetype/list/', RealEstateTypeListAPIView.as_view()),
    path('properties/list', Realestate_All_BuyAPIView.as_view()),
]
