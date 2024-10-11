from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Realestate_All_Buy
from rest_framework import serializers
from .models import RealEstateType
from .models import Realestate_All_Buy

# Create your views here.

class RealEstateTypeListAPIView(APIView):
    def get(self, request):
        properties = Realestate_All_Buy.objects.all()
        serializer = PropertiesSerializer(properties, many=True)
        return Response(serializer.data)


class RealEstateTypeSerializer (serializers.ModelSerializer):
    class Meta:
        model = RealEstateType
        fields =  '__all__'

class Realestate_All_BuyAPIView(APIView):
    def get(self, request):
        types = Realestate_All_Buy.objects.all()
        serializer = PropertiesSerializer(types, many=True)
        return Response(serializer.data)

class PropertiesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Realestate_All_Buy
        fields =  '__all__'
    
