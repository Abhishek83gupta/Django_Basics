from django.contrib import admin
from .models import Company
 
@admin.register(Company)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_no', 'company_type' )
    search_fields = ('name', 'address', 'phone_no', 'company_type' )


