from django.db import models
from formation_area.models.formation_area_model import FormationArea
from formation_area.models.sub_formation_area_model import SubFormationArea
from formation_area.models.formation_environment_model import FormationEnvironment
from utils.models import BaseSlugTitleModel
from user.models import User


class ShawProcess(BaseSlugTitleModel):

    formation_area = models.ForeignKey(
        FormationArea,
        related_name='shaw_processes',
        on_delete=models.CASCADE
    )

    sub_formation_area = models.ForeignKey(
        SubFormationArea,
        related_name='shaw_processes',
        on_delete=models.CASCADE
    )

    formation_environment = models.ForeignKey(
        FormationEnvironment,
        related_name='shaw_processes',
        on_delete=models.CASCADE
    )

    created_by = models.ForeignKey(
        User,
        related_name='shaw_processes',
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=50)
    date = models.DateField()
    danger_factor = models.CharField(max_length=255)
    danger_source = models.CharField(max_length=255)
    danger = models.CharField(max_length=255)
    occupational_risk = models.CharField(max_length=255)
    risk_source = models.CharField(max_length=255)
    workers_exposed = models.PositiveSmallIntegerField()
    exposure_time = models.CharField(max_length=255)
    occurrence_probability = models.CharField(max_length=255)
    consequences = models.CharField(max_length=255)
    danger_degree = models.CharField(max_length=255)
    risk_degree = models.CharField(max_length=255)
    danger_description = models.CharField(max_length=255)

    class Meta:
        db_table = 'shaw_process'
        verbose_name = 'shaw_process'
        verbose_name_plural = 'shaw_processes'
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'formation_area',
                    'sub_formation_area',
                    'formation_environment',
                    'title',
                ],
                name='unique_shaw_title_per_formation_environment'
            )
        ]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/{self.slug}'
    
    def get_formation_area(self):
        return self.formation_area.name
    
    def get_sub_formation_area_name(self):
        return self.sub_formation_area.name
    
    def get_formation_environment_name(self):
        return self.formation_environment.name
    
    def save(self, *args, **kwargs):
        self.sub_formation_area = self.formation_environment.sub_formation_area
        self.formation_area = self.sub_formation_area.formation_area
        return super().save(*args, **kwargs)
