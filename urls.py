from django.urls import path
from realhomebackend.views import RealEstateTypeListAPIView

urlpatterns = [
    path('realestatetype/list/', RealEstateTypeListAPIView.as_view())
]
