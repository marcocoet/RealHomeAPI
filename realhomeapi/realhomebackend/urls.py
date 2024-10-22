from django.urls import path
from realhomebackend.views import RealEstateTypeListAPIView
from realhomebackend.views import UsersAPIView
from realhomebackend.views import LoginAPIView
from realhomebackend.views import Home


urlpatterns = [
    path('realestatetype/list/', RealEstateTypeListAPIView.as_view()),
    path('users/', UsersAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    #path('realestate/', RealEstateAddAPIView)
    path('home', Home.as_view()),
]
