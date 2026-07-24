from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    SmartPriceTrackerAPI uchun maxsus foydalanuvchi modeli.
    """

    email = models.EmailField(
        verbose_name="Email pochta", unique=True, max_length=255
    )
    first_name = models.CharField(
        verbose_name="Ism", max_length=150, blank=True
    )
    last_name = models.CharField(
        verbose_name="Familiya", max_length=150, blank=True
    )

    # Ruxsatlar uchun Django tizim tekshiruvlari
    is_active = models.BooleanField(verbose_name="Faol", default=True)
    is_staff = models.BooleanField(
        verbose_name="Adminlik huquqi", default=False
    )
    date_joined = models.DateTimeField(
        verbose_name="Ro'yxatdan o'tgan sanasi", auto_now_add=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"  # Usernameni almashtiradigan buyruq
    REQUIRED_FIELDS = []  # Superuser yaratishda so'raladigan talablar (standart ravishda email va parol)

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
        ordering = ["-date_joined"]

    def __str__(self):
        return self.email

