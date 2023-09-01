from django.contrib import admin
from .models import EnvironmentalProccess

@admin.register(EnvironmentalProccess)
class EnvironmentalProccessAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}