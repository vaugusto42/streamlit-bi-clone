from rest_framework import serializers
from .models import Company, User

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company 
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = '__all__'