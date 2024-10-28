from django.contrib.auth.models import User
from rest_framework import serializers
from .models import RealEstateType
from .models import NewRealEstate


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  '__all__'
        
class UsersSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        print("A1")
        print(attrs)
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Password don't match")
        
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = super().create(validated_data)
        user.set_password(validated_data.pop('password'))
        user.save()
        return user

    class Meta:
        model = User
        fields =  ['email', 'username', 'password', 'confirm_password', 'first_name', 'last_name']
        
class NewRealEstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewRealEstate
        fields = '__all__' 
        
class RealEstateTypeSerializer (serializers.ModelSerializer):
    class Meta:
        model = RealEstateType
        fields =  '__all__'