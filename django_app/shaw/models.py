from django.db import models
from formation_area.models import SubFormationArea, FormationArea, FormationEnvironment
from utils.models import BaseModel

class ShawProcess(BaseModel):
    class Status(models.TextChoices):
        ACTIVE = 'AT', 'Active'
        INACTIVE = 'IN', 'Inactive'

    formation_area = models.ForeignKey(
        FormationArea,
        related_name='shaw_proccesses',
        on_delete=models.CASCADE
    )

    sub_formation_area = models.ForeignKey(
        SubFormationArea,
        related_name='shaw_proccesses',
        on_delete=models.CASCADE
    )

    formation_environment = models.ForeignKey(
        FormationEnvironment,
        related_name='shaw_proccesses',
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=255)
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

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.INACTIVE
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/{self.formation_area}/{self.sub_formation_area}/{self.formation_environment}/{self.slug}'