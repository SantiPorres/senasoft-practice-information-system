from django.db import models
from django.template.defaultfilters import slugify

from django.db.models.query import QuerySet
from uuid import uuid4


class ActiveManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(
            status = BaseModel.Status.ACTIVE
        )

class BaseModel(models.Model):

    class Status(models.TextChoices):
        ACTIVE = 'AT', 'Active'
        INACTIVE = 'IN', 'Inactive'

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )

    slug = models.SlugField(
        unique=True, 
        default=str(uuid4()),
        max_length=100,
        db_index=True
    )

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.ACTIVE
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    active = ActiveManager()

    class Meta:
        abstract = True

    def __str__(self):
        return self.slug
        

class BaseSlugNameModel(BaseModel):
    def save(self, *args, **kwargs):
        name_uuid_slugify = f'{slugify(self.name)}-{uuid4().hex[:6]}'
        self.slug = name_uuid_slugify
        return super().save(*args, **kwargs)
    
    class Meta:
        abstract = True
    

class BaseSlugTitleModel(BaseModel):
    def save(self, *args, **kwargs):
        title_uuid_slugify = f'{slugify(self.title)}-{uuid4().hex[:6]}'
        self.slug = title_uuid_slugify
        return super().save(*args, **kwargs)
    
    class Meta:
        abstract = True
