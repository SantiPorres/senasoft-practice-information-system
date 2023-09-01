from django.db import models
import uuid


class BaseModel(models.Model):
    slug = models.SlugField(
        unique=True, 
        default=str(uuid.uuid4())
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)