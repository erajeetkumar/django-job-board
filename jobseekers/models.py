from django.db import models

# Create your models here.
# Create JobSeeker model
class JobSeeker(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.FileField(upload_to='cover_letters/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.OneToOneField('common.CustomUser', on_delete=models.CASCADE, related_name='job_seeker')
    def __str__(self):
        return f"{self.first_name} {self.last_name}"