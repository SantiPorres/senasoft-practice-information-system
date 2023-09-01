from django.contrib import admin
from .models import ShawProcess

@admin.register(ShawProcess)
class ShawProccessAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
