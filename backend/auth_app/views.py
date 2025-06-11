from django.shortcuts import render
from rest_framework import generics
from .models import Company, User
from .serializers import CompanySerializer, UserSerializer

class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
