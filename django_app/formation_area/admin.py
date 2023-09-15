from django.contrib import admin
from .models import FormationArea, SubFormationArea, FormationEnvironment


@admin.register(FormationArea)
class FormationAreaAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'description',
        'status',
    ]

@admin.register(SubFormationArea)
class SubFormationAreaAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'description',
        'status',
        'formation_area',
    ]


@admin.register(FormationEnvironment)
class FormationEnvironmentAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'capacity',
        'status',
        'sub_formation_area',
    ]
