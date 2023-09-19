from django.db import models
from utils.models import BaseSlugNameModel
import uuid


class FormationArea(BaseSlugNameModel):

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

    class Meta:
        db_table = 'formation_area'
        verbose_name = 'formation_area'
        verbose_name_plural = 'formation_areas'
    
    def get_absolute_url(self):
        return f'api/formation-area/{self.slug}/'
