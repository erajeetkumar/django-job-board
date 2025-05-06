from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.core.validators import validate_email
from .serializers import CustomUserSerializer

# Create your views here.
#handle user registration using UserSerializer
class UserRegistrationView(CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = []
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
