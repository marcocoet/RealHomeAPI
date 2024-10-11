from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import serializers
from .models import RealEstateType
from .models import RealEstate


# Create your views here.




class RealEstateTypeSerializer (serializers.ModelSerializer):
    class Meta:
        model = RealEstateType
        fields =  '__all__'

    def get(self, request):
class RealEstateAddAPIView(APIView):
    def post(self, request):
        print("Hallo1")
        serializer = RealEstateAddSerializer(data=request.data)
        print("Hallo1a")
        if serializer.is_valid():
            serializer.save()
            print("Hallo2")
            #savedRealEstate = serializer.instance
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

class RealEstateAddSerializer (serializers.ModelSerializer):
    class Meta:
        model = RealEstate
        fields =  ['address', 'bathrooms', 'bedrooms', 'landSqm',
                   'floorSqm', 'parking', 'shortDescription', 'longDescription']

class RealEstateTypeSerializer (serializers.ModelSerializer):
    class Meta:
        model = RealEstateType
        fields =  '__all__'


    
