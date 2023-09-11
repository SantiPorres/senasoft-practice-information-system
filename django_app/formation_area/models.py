from django.db import models
from utils.models import BaseFormationAreaSubEnvironmentModel
import uuid


class FormationArea(BaseFormationAreaSubEnvironmentModel):

    name = models.CharField(
        max_length=36, 
        default=str(uuid.uuid4()),
        unique=True
    )
    description = models.CharField(max_length=1000)

    class Meta:
        db_table = 'formation_area'
        verbose_name = 'formation_area'
        verbose_name_plural = 'formation_areas'
    
    def get_absolute_url(self):
        return f'/{self.slug}'


class SubFormationArea(BaseFormationAreaSubEnvironmentModel):

    name = models.CharField(
        max_length=36, 
        default=str(uuid.uuid4()),
        unique=True
    )
    description = models.CharField(max_length=1000)

    formation_area = models.ForeignKey(
        FormationArea, 
        related_name='sub_formation_areas', 
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'sub_formation_area'
        verbose_name = 'sub_formation_area'
        verbose_name_plural = 'sub_formation_areas'
    
    def get_absolute_url(self):
        return f'/{self.formation_area}/{self.slug}'


class FormationEnvironment(BaseFormationAreaSubEnvironmentModel):

    name = models.CharField(
        max_length=36, 
        default=str(uuid.uuid4()),
        unique=True
    )
    capacity = models.PositiveSmallIntegerField(default=5)

    formation_area = models.ForeignKey(
        FormationArea, 
        related_name='formation_environments', 
        on_delete=models.CASCADE
    )

    sub_formation_area = models.ForeignKey(
        SubFormationArea,
        related_name='formation_environments',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'formation_environment'
        verbose_name = 'formation_environment'
        verbose_name_plural = 'formation_environments'

    def get_absolute_url(self):
        return f'/{self.formation_area}/{self.sub_formation_area}/{self.slug}/{self.id}'
