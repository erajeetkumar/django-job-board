from rest_framework import serializers
from common.models import CustomUser as User
from employers.models import Company, Employer
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from django.contrib.auth.hashers import make_password

#implement logging  
import logging
logger = logging.getLogger(__name__)
# Create your serializers here.

class EmployerRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    phone_number = serializers.CharField(max_length=17, required=False)
    password = serializers.CharField(write_only=True, min_length=6)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def create(self, validated_data):
        try:
            validate_email(validated_data['email'])
        except ValidationError:
            raise serializers.ValidationError("Invalid email format.")

        try:
            user = User.objects.get(email=validated_data['email'])
            if user.is_employer:
                raise serializers.ValidationError("Email already exists.")
        except User.DoesNotExist:
            pass
        except Exception as e:
            logger.error(f"Error creating user: {e}")
            raise serializers.ValidationError("An error occurred while creating the user.")

        try:
            user = User.objects.create_user(
                email=validated_data['email'],
                password=validated_data['password'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                phone_number=validated_data.get('phone_number', ''),
                is_employer=True
            )
        except Exception as e:
            logger.error(f"Error creating user: {e}")
            raise serializers.ValidationError("An error occurred while creating the user.")

        logger.info(f"User created: {user.email}")

        

        return user
    
    
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'description', 'address', 'logo', 'website', 'phone_number']
        extra_kwargs = {
            'logo': {'required': False},
            'website': {'required': False},
            'phone_number': {'required': False}
        }
    def validate_name(self, value):
        if Company.objects.filter(name=value).exists():
            raise serializers.ValidationError("Company name already exists.")
        return value
    def validate(self, attrs):
        if 'name' in attrs:
            name = attrs['name']
            try:
                self.validate_name(name)
            except ValidationError:
                raise serializers.ValidationError("Invalid company name format.")
        return attrs
    
    def validate_logo(self, value):
        if value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError("Logo size exceeds 5MB.")
        return value
    
    def create(self, validated_data):
        try:
            company = Company.objects.create(
                name=validated_data['name'],
                description=validated_data.get('description', ''),
                address=validated_data.get('address', ''),
                
                phone_number=validated_data.get('phone_number', ''),
                created_by=self.context['request'].user
            )
        except Exception as e:
            logger.error(f"Error creating company: {e}")
            raise serializers.ValidationError("An error occurred while creating the company.")

        logger.info(f"Company created: {company.name}")

        return company  