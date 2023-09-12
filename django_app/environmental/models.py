from django.db import models
from formation_area.models import SubFormationArea, FormationArea, FormationEnvironment
from user.models import User
from utils.models import BaseSlugTitleModel

class EnvironmentalProccess(BaseSlugTitleModel):

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

    formation_environment = models.ForeignKey(
        FormationEnvironment,
        related_name='environmental_proccesses',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    created_by = models.ForeignKey(
        User,
        related_name='environmental_proccesses',
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=50)
    date = models.DateField()
    activity = models.CharField(max_length=255)
    environmental_aspect = models.CharField(max_length=255)
    impact = models.CharField(max_length=255)
    impact_description = models.CharField(max_length=255)
    recoverability = models.CharField(max_length=255)
    classification = models.CharField(max_length=255)
    nature = models.CharField(max_length=255)
    observations = models.CharField(max_length=255)

    class Meta:
        db_table = 'environmental_proccess'
        verbose_name = 'environmental_proccess'
        verbose_name_plural = 'environmental_proccesses'
    
    def get_absolute_url(self):
        return f'/{self.formation_area}/{self.sub_formation_area}/{self.slug}'