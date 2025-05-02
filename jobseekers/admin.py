from django.contrib import admin

# Register models here.
from .models import JobSeeker
#@admin.register(JobSeeker)
class JobSeekerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
# Register the models with the admin site
admin.site.register(JobSeeker, JobSeekerAdmin)
