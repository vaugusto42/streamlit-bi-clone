from django.urls import path 
from .views import CompanyListAPIView, UserListAPIView

urlpatterns = [
    path('companies/', CompanyListAPIView.as_view(), name='company-list'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
]

