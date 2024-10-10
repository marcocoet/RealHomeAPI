from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Realestate_All_Buy
from rest_framework import serializers
from django.http import Http404
import requests

# Serializer for the Properties model
class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestate_All_Buy
        fields = '__all__'

# API to handle GET (all properties), POST (add property)
class PropertiesListCreateAPIView(APIView):
    def get(self, request):
        properties = Realestate_All_Buy.objects.all()
        serializer = PropertiesSerializer(properties, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PropertiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API to handle GET (single property), PUT (update property), DELETE (delete property)
class PropertiesDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Realestate_All_Buy.objects.get(pk=pk)
        except Realestate_All_Buy.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        property = self.get_object(pk)
        serializer = PropertiesSerializer(property)
        return Response(serializer.data)

    def put(self, request, pk):
        property = self.get_object(pk)
        serializer = PropertiesSerializer(property, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        property = self.get_object(pk)
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Geocoding API endpoint
class GeocodeAPIView(APIView):
    def get(self, request, address):
        api_key = "AIzaSyBmAfCozYlecVlX38GvA5audqHXMiE7Ums"
        base_url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {
            'address': address,
            'key': api_key
        }
        response = requests.get(base_url, params=params)
        return Response(response.json(), status=status.HTTP_200_OK)
