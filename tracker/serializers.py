from rest_framework import serializers
from .models import TrackedProduct

class TrackedProductSerializer(serializers.ModelSerializer):
    """Kuzatilayotgan mahsulot modeli uchun serializator."""

    # Foydalanuvchi maydonini faqat o'qish uchun mo'ljallaymiz, shunda hech kim POST so'rovi orqali egasini soxtalashtira olmaydi.
    user = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = TrackedProduct
        fields = [
            "id",
            "user",
            "title",
            "url",
            "current_price",
            "update_interval",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "current_price", "created_at", "updated_at"]

    def validate_url(self, value):
        """URL tasdig'i: tuzilma bo'yicha havola ishlayotganini tekshiramiz."""
        if not value.startswith("http://") and not value.startswith("https://"):
            raise serializers.ValidationError(
                "Havola http:// yoki https:// bilan boshlanishi shart."
            )
        return value
