from django.contrib import admin
from .models import FormationArea, SubFormationArea, FormationEnvironment


@admin.register(FormationArea)
class FormationAreaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(SubFormationArea)
class SubFormationAreaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(FormationEnvironment)
class FormationEnvironmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
