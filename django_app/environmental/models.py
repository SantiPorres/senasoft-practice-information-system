from django.db import models
from formation_area.models import SubFormationArea, FormationArea
from utils.models import BaseModel

class EnvironmentalProccess(BaseModel):
    class Status(models.TextChoices):
        ACTIVE = 'AT', 'Active'
        INACTIVE = 'IN', 'Inactive'

    formation_area = models.ForeignKey(
        FormationArea,
        related_name='environmental_proccesses',
        on_delete=models.CASCADE
    )

    sub_formation_area = models.ForeignKey(
        SubFormationArea,
        related_name='environmental_proccesses',
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=255)
    date = models.DateField()
    activity = models.CharField(max_length=255)
    environmental_aspect = models.CharField(max_length=255)
    impact = models.CharField(max_length=255)
    impact_description = models.CharField(max_length=255)
    recoverability = models.CharField(max_length=255)
    classification = models.CharField(max_length=255)
    nature = models.CharField(max_length=255)
    observations = models.CharField(max_length=255)

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.INACTIVE
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/{self.formation_area}/{self.sub_formation_area}/{self.slug}'