from django.shortcuts import render

#create api view to register employer
from django.http import JsonResponse
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .serializers import EmployerRegistrationSerializer, CompanySerializer
from drf_yasg.utils import swagger_auto_schema

from .models import Employer, Company

#create permission class to check if user is employer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission

class IsEmployer(BasePermission):
        def has_permission(self, request, view):
            return request.user.is_employer == True



@swagger_auto_schema(request_body=EmployerRegistrationSerializer)
class EmployerRegistrationView(CreateAPIView):
    serializer_class = EmployerRegistrationSerializer
    permission_classes = []
    
    def post(self, request):
        serializer = EmployerRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Employer registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


 # Create CompanyCreateAPIView
class CompanyCreateAPIView(CreateAPIView):
    serializer_class = CompanySerializer
    
    #permission is IsAuthenticated and isEmployer
    permission_classes = [IsAuthenticated, IsEmployer]
    
    def post(self, request):
        serializer = CompanySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Company created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
