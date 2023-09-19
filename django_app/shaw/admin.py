from django.contrib import admin
from .models import ShawProcess

@admin.register(ShawProcess)
class ShawProcessAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
