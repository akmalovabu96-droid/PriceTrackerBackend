from django.db import models
from django.conf import settings

# Create your models here.

class TrackedProduct(models.Model):
    """Foydalanuvchi narxlarni kuzatish uchun qo‘shgan mahsulot modeli."""

    # Mahsulotni kastom foydalanuvchimiz bilan bog'laymiz
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tracked_products",
        verbose_name="Foydalanuvchi",
    )

    title = models.CharField(
        verbose_name="Mahsulot nomi", max_length=255, blank=True
    )
    url = models.URLField(verbose_name="Mahsulot havolasi", max_length=1000)

    # Joriy yaroqli narx
    current_price = models.DecimalField(
        verbose_name="Joriy narx",
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )

    # Tekshiruv oralig‘i (daqiqa) (masalan: 60, 360, 1440)
    update_interval = models.PositiveIntegerField(
        verbose_name="Yangilanish oralig'i (daqiqada)", default=1440
    )

    is_active = models.BooleanField(
        verbose_name="Kuzatuv statusi", default=True, db_index=True
    )

    created_at = models.DateTimeField(
        verbose_name="Qo'shilish sanasi", auto_now_add=True
    )
    updated_at = models.DateTimeField(verbose_name="Yangilanish sanasi", auto_now=True)

    class Meta:
        verbose_name = "Kuzatilayotgan mahsulot"
        verbose_name_plural = "Kuzatilayotgan mahsulotlar"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title or self.url


class PriceHistory(models.Model):
    """Tahlil uchun mo'ljallangan narxlar va mahsulotlarning o'zgarish hikoyasi."""

    # Aniq kuzatilayotgan mahsulot bilan bog'lanish
    product = models.ForeignKey(
        TrackedProduct,
        on_delete=models.CASCADE,
        related_name="price_history",
        verbose_name="Hikoya",
    )

    price = models.DecimalField(
        verbose_name="Belgilangan narx", max_digits=12, decimal_places=2
    )

    # Narx belgilangan vaqti (grafiklarda sana bo'yicha tez saralanishi uchun indeks ishlatiladi)
    recorded_at = models.DateTimeField(
        verbose_name="Saqlash vaqti", auto_now_add=True, db_index=True
    )

    class Meta:
        verbose_name = "Narx hikoyasi"
        verbose_name_plural = "Narxlar hikoyasi"
        ordering = ["-recorded_at"]

    def __str__(self):
        return f"{self.product.title or 'Mahsulot'} - {self.price} ({self.recorded_at.strftime('%d.%m.%Y %H:%M')})"

