from realhomebackend.models import RealEstateType
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from .models import RealEstateType

 

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

