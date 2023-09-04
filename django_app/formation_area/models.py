from django.db import models
from utils.models import BaseModel
import uuid


class FormationArea(BaseModel):
    class Status(models.TextChoices):
        ACTIVE = 'AT', 'Active'
        INACTIVE = 'IN', 'Inactive'

    name = models.CharField(max_length=25, default=str(uuid.uuid4()))
    description = models.CharField(max_length=1000)

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.INACTIVE
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}'


class SubFormationArea(BaseModel):
    class Status(models.TextChoices):
        ACTIVE = 'AT', 'Active'
        INACTIVE = 'IN', 'Inactive'

    name = models.CharField(max_length=25, default=str(uuid.uuid4()))
    description = models.CharField(max_length=1000)

    formation_area = models.ForeignKey(
        FormationArea, 
        related_name='sub_formation_areas', 
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.INACTIVE
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.formation_area}/{self.slug}'


class FormationEnvironment(BaseModel):
    class Status(models.TextChoices):
        ACTIVE = 'AT', 'Active'
        INACTIVE = 'IN', 'Inactive'

    name = models.CharField(max_length=25, default=str(uuid.uuid4()))
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

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.INACTIVE
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.formation_area}/{self.sub_formation_area}/{self.slug}/{self.id}'
