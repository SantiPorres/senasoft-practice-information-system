from django.db import models
from utils.models import BaseSlugNameModel
import uuid

from .formation_area_model import FormationArea
from .sub_formation_area_model import SubFormationArea


class FormationEnvironment(BaseSlugNameModel):

    name = models.CharField(
        max_length=36, 
        default=str(uuid.uuid4()),
        null=False,
        blank=False
    )

    capacity = models.PositiveSmallIntegerField(
        default=5,
        null=False,
        blank=False
    )

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
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'sub_formation_area',
                    'name'
                ],
                name='unique_name_per_sub_formation_area'
            )
        ]

    def get_absolute_url(self):
        return f'api/formation-area/{self.formation_area}/sub-formation-area/{self.sub_formation_area}/formation-environment/{self.slug}/'

    def get_formation_area_slug(self):
        return self.formation_area.slug
    
    def get_sub_formation_area_slug(self):
        return self.sub_formation_area.slug
