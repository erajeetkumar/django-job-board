from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

#create an API view for the jobseekers app  
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import JobSeeker
from .serializers import JobSeekerSerializer
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator

class JobSeekerList(APIView):
    """
    List all job seekers, or create a new job seeker.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        job_seekers = JobSeeker.objects.all()
        serializer = JobSeekerSerializer(job_seekers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobSeekerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)