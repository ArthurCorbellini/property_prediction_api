"""
Database models.
"""
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    # substitui o username pelo email no login pelo django
    USERNAME_FIELD = "email"


class RealEstate(models.Model):
    """RealEstate object."""
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True
    )
    city = models.CharField(max_length=255)
    area = models.IntegerField()
    qt_rooms = models.IntegerField()
    qt_bathrooms = models.IntegerField()
    qt_parking_spaces = models.IntegerField()
    floor = models.IntegerField()
    allows_animals = models.BooleanField()
    furnished = models.BooleanField()
    vl_hoa = models.DecimalField(max_digits=10, decimal_places=2)
    vl_rent = models.DecimalField(max_digits=10, decimal_places=2)
    vl_tax = models.DecimalField(max_digits=10, decimal_places=2)
    vl_fire_insurance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.city + " " + self.area + " " + self.vl_rent)
