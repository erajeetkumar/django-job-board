from django.contrib import admin

# Register your models here.

#register employer model
from .models import Employer, Company
#@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('company', 'contact_person', 'email', 'phone_number', 'address', 'website', 'created_at', 'updated_at')
    search_fields = ('company__name', 'contact_person', 'email')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

#@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'logo', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
# Register the models with the admin site
admin.site.register(Employer, EmployerAdmin)
admin.site.register(Company, CompanyAdmin)
