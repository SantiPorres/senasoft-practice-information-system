from typing import Any
from django.db import models
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group
from django.http import Http404
from enum import Enum
from django.dispatch import receiver
from django.db.models.signals import post_save

from utils.constants import PASSWORD_HASH_BEGINNING


class CustomUserManager(BaseUserManager):
    def _create_user(self, personal_id_number, email, password, first_name, last_name, mobile, **extra_fields):
        if not personal_id_number:
            raise ValueError('Personal id number must be provided')
        if not password:
            raise ValueError('Password must be provided')
        
        user = self.model(
            personal_id_number = personal_id_number,
            email = self.normalize_email(email),
            first_name = 'esto es una prueba',
            last_name = last_name,
            mobile = mobile,
            **extra_fields
        )
        
        user.set_password(password)
        user.save(using=self._db)

        """if role == 'instructor':
            print('user.role')
            try:
                instructors_group = Group.objects.get(name='instructors')
            except Group.DoesNotExist:
                raise Http404
            instructors_group.user_set.add(user)"""

        return user
    
    def create_user(self, personal_id_number, email, password, first_name, last_name, mobile, **extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(personal_id_number, email, password, first_name, last_name, mobile, **extra_fields)
    
    def create_superuser(self, personal_id_number, email, password, first_name, last_name, mobile, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(personal_id_number, email, password, first_name, last_name, mobile, **extra_fields)


class Role(Enum):
    ADMINISTRATOR = 'administrator'
    INSTRUCTOR = 'instructor'


class User(AbstractBaseUser, PermissionsMixin):

    personal_id_number = models.CharField(db_index=True, unique=True, max_length=20)
    email = models.EmailField(max_length=130)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=30)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    """default_role = Role.INSTRUCTOR
    role = models.CharField(
        max_length=15,
        choices=[(tag.value, tag.name) for tag in Role],
        default=Role.INSTRUCTOR.value
    )"""

    objects = CustomUserManager()

    USERNAME_FIELD = 'personal_id_number'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'mobile']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def save(self, *args, **kwargs):
        if self.password[:13] != PASSWORD_HASH_BEGINNING:
            self.password = make_password(self.password)

        super().save(*args, **kwargs)

        """if self.role == Role.INSTRUCTOR.value:
            group = Group.objects.get(name='instructors')
            self.groups.add(group)
            print(self.groups.all())"""
            

"""@receiver(post_save, sender=User)
def assign_group(sender, instance, **kwargs):
    group = Group.objects.get(name='instructors')
    instance.groups.add(group)
    instance.save()"""