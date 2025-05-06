from django.urls import path
from . import views

urlpatterns = [
    
    
    #include API views
    path('api/jobseekers/', views.JobSeekerList.as_view(), name='job_seeker_list'),
    
]