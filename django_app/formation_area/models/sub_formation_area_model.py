from django.db import models
from utils.models import BaseSlugNameModel
import uuid

from .formation_area_model import FormationArea


class SubFormationArea(BaseSlugNameModel):

    name = models.CharField(
        max_length=36, 
        default=str(uuid.uuid4()),
        unique=True,
        null=False,
        blank=False
    )
    description = models.TextField(
        max_length=1000,
        null=True,
        blank=True
    )

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
        return f'api/formation-area/{self.formation_area}/sub-formation-area/{self.slug}/'
    
    def get_formation_area_slug(self):
        return self.formation_area.slug
