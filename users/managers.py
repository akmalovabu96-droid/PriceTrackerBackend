from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Avtorizatsiya uchun username o'rniga
    email noyob identifikator bo'lib xizmat
    qiladigan maxsus foydalanuvchi menejeri
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Foydalanuvchida Email bo'lishi shart.")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields["is_staff"] = True
        extra_fields["is_superuser"] = True
        extra_fields["is_active"] = True

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuserda is_staff=True bo'lishi shart.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuserda is_superuser=True bo'lishi shart.")

        return self.create_user(email, password, **extra_fields)
