from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.db import models
import pyotp


class UserManager(BaseUserManager):
    def create_user(self, email, username, name, password, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        if not name:
            raise ValueError("Users must have a name")
        if not password:
            raise ValueError("Users must have a password")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, password, **extra_fields):
        if not password:
            raise ValueError("Superusers must have a password")

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, username, name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    otp_secret = models.CharField(max_length=32, default=pyotp.random_base32)
    is_2fa_enabled = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "name"]  # Used by createsuperuser

    objects = UserManager()

    def __str__(self):
        return self.email
