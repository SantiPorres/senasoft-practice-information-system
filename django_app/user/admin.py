from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['personal_id_number', 'last_name', 'first_name', 'email', 'mobile']
    #search_fields = ['__all__']
    ordering = ['last_name', 'first_name']    
