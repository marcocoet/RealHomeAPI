from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RealEstateType
from .serializers import RealEstateTypeSerializer, UsersSerializer, RealEstateAddSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny

# Create your views here.
class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        user = authenticate(request=request, username=username, password=password)
        print("H4")
        print(user)
        if user is not None:
            
            return Response("Login Successfull")
        else:
            return Response("Login Unsuccessfull", status=400)

class RealEstateTypeListAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        types = RealEstateType.objects.all()
        serializer = RealEstateTypeSerializer(types, many=True)
        return Response(serializer.data)

class UsersAPIView(APIView):
    def post(self, request):
        print("request.data:")
        print(request.data)
        serializer = UsersSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            
            #savedRealEstate = serializer.instance
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
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