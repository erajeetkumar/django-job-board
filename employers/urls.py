from django.urls import path
from . import views

app_name = 'employers'

urlpatterns = [
    #add employer registration view
    #path('register/', views.EmployerRegistrationView.as_view(), name='employer_registration'),
    #company create view
    path('company/create/', views.CompanyCreateAPIView.as_view(), name='company_create'),
    
]