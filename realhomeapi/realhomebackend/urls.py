from django.urls import path
from realhomebackend.views import RealEstateTypeListAPIView
from realhomebackend.views import UsersAPIView
from realhomebackend.views import LoginAPIView
from realhomebackend.views import Home
from realhomebackend.views import NewRealEstateAddAPIView



urlpatterns = [
    path('realestatetype/list/', RealEstateTypeListAPIView.as_view()),
    path('users/', UsersAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('add-real-estate/', NewRealEstateAddAPIView.as_view()),
    path('home', Home.as_view()),
    ]
