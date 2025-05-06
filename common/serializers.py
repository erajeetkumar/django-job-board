from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

CustomUser = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'is_employer']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value
    
    def validate(self, attrs):
        if 'email' in attrs:
            email = attrs['email']
            try:
                self.validate_email(email)
            except ValidationError:
                raise serializers.ValidationError("Invalid email format.")
        return attrs
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            
            email=validated_data['email'],
            password= make_password(validated_data['password']),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            is_employer=validated_data.get('is_employer', False)
        )
        return user