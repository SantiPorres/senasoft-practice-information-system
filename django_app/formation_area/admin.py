from django.contrib import admin
from .models.formation_environment_model import FormationEnvironment
from .models.formation_area_model import FormationArea
from .models.sub_formation_area_model import SubFormationArea


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
