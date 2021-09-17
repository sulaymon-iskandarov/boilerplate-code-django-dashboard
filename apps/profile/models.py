from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class ProfileManager(BaseUserManager):
    """
        Custom user model manager where email is the unique identifiers
        for authentication instead of usernames.
        """

    def create_user(self, email, username, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, username=username, **extra_fields)


class Profile(AbstractUser):
    """
    The User model has already:
    - first name
    - last name
    - email
    - username
    """

    birthday = models.DateField(auto_now=False, blank=True, null=True)
    gender = models.CharField(max_length=35, blank=True, null=True)
    phone = models.CharField(max_length=35, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    address_number = models.CharField(max_length=35, blank=True, null=True)
    city = models.CharField(max_length=35, blank=True, null=True)
    zip = models.CharField(max_length=35, blank=True, null=True)
    user_photo = models.ImageField(upload_to=settings.DEFAULT_FILE_IMAGE_STORAGE, null=True, blank=True)

    objects = ProfileManager()