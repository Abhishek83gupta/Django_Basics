from django.contrib import admin
from .models import College
 
@admin.register(College)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('collage_name', 'address', 'phone_no')
    search_fields = ('collage_name', 'address', 'phone_no' )