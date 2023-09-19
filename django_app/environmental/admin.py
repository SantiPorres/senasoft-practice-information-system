from django.contrib import admin
from .models import EnvironmentalProcess

@admin.register(EnvironmentalProcess)
class EnvironmentalProcessAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}