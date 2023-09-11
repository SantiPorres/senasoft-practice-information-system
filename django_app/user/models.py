from django.db import models
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    def _create_user(self, personal_id_number, email, password, first_name, last_name, mobile, **extra_fields):
        if not personal_id_number:
            raise ValueError('Personal id number must be provided')
        if not password:
            raise ValueError('Password must be provided')
        
        user = self.model(
            personal_id_number = personal_id_number,
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            mobile = mobile,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
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


class User(AbstractBaseUser, PermissionsMixin):

    """class Rol(models.TextChoices):
        ADMINISTRATOR = 'Administrator', 'ADMINISTRATOR'
        INSTRUCTOR = 'Instructor', 'INSTRUCTOR'"""

    personal_id_number = models.CharField(db_index=True, unique=True, max_length=20)
    email = models.EmailField(max_length=130)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=30)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    """default_rol = Rol.INSTRUCTOR
    rol = models.CharField(
        max_length=13,
        choices=Rol.choices,
        default=default_rol
    )"""

    USERNAME_FIELD = 'personal_id_number'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'mobile']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def save(self, *args, **kwargs):
        if self.password[:13] == 'pbkdf2_sha256':
           return super().save(*args, **kwargs)
        else:
            self.password = make_password(self.password)
            return super().save(*args, **kwargs)