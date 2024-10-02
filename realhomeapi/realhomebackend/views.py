from realhomebackend.models import RealEstateType
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from .models import RealEstateType
from .models import Properties

# Create your views here.

class RealEstateTypeListAPIView(APIView):
    def get(self, request):
        types = RealEstateType.objects.all()
        serializer = RealEstateTypeSerializer(types, many=True)
        return Response(serializer.data)


class RealEstateTypeSerializer (serializers.ModelSerializer):
    class Meta:
        model = RealEstateType
        fields =  '__all__'

class PropertiesAPIView(APIView):
    def get(self, request):
        types = Properties.objects.all()
        serializer = PropertiesSerializer(types, many=True)
        return Response(serializer.data)

class PropertiesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields =  '__all__'
    
