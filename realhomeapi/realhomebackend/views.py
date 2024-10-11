from realhomebackend.models import RealEstateType
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from .models import RealEstateType
from .models import Users
from .models import RealEstate
# Create your views here.

class RealEstateTypeListAPIView(APIView):
    def get(self, request):
        types = RealEstateType.objects.all()
        serializer = RealEstateTypeSerializer(types, many=True)
        return Response(serializer.data)
    
class UsersListAPIView(APIView):
    def get(self, request):
        types = Users.objects.all()
        serializer = UsersSerializer(types, many=True)
        return Response(serializer.data)

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

    
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields =  '__all__'
