from django.urls import path
from realhomebackend.views import RealEstateTypeListAPIView
from realhomebackend.views import RealEstateAddAPIView
#from .views import UsersListAPIView


urlpatterns = [
    path('realestatetype/list/', RealEstateTypeListAPIView.as_view()),
    #path('users/list/', UsersListAPIView.as_view()),
    path('realestate/add/', RealEstateAddAPIView.as_view())
]
