from django.db import models

# Create your models here.

#the company model
#should belong to the employer
# Create a model for the Company

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='company_logos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Create a model for the Employer
class Employer(models.Model):
    company = models.OneToOneField('employers.Company', on_delete=models.CASCADE, related_name='employer')
    contact_person = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.OneToOneField('common.CustomUser', on_delete=models.CASCADE, related_name='employer')

    def __str__(self):
        return self.company_name