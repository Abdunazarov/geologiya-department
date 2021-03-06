from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models


# Create superuser with email instead of username
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    inn = models.CharField(max_length=100)
    name_parsed = models.CharField(max_length=250)
    category_business = models.CharField(max_length=500)
    city = models.CharField(max_length=10)
    cn = models.CharField(max_length=100)
    email = models.EmailField(_('email address'), unique=True)
    image = models.ImageField(default="/default.jpg")
    organization = models.CharField(max_length=500)
    serial_number = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    path = models.CharField(max_length=250)
    valid_form = models.DateTimeField(null=True)
    valid_to = models.DateTimeField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

