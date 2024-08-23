from django.contrib import admin
from .models import STUDENT
 
@admin.register(STUDENT)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_no' , 'college_name')
    search_fields = ('name', 'address', 'phone_no', 'college_name')