from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import TrackedProduct
from .serializers import TrackedProductSerializer

# Create your views here.

class TrackedProductViewSet(viewsets.ModelViewSet):
    """
    Joriy foydalanuvchining kuzatilayotgan mahsulotlarini
    yaratish, ko'rish, yangilash va o'chirish uchun
    mo'ljallangan maxsus ViewSet.
    """

    serializer_class = TrackedProductSerializer
    permission_classes = [IsAuthenticated]  # Endpointni avtorizatsiya bilan himoyalaymiz

    def get_queryset(self):
        """
        Izolyatsiya: Mahsulotlarni FAQATGINA
        joriy avtorizatsiyalangan foydalanuvchiga
        qaytaramiz. Shunda boshqa birovlar uning
        faoliyatini kuzata olmaydi.
        """
        # Agar foydalanuvchi avtorizatsiyalanmagan bo'lsa, bo'm-bo'sh ro'yxat chiqariladi
        if self.request.user.is_anonymous:
            return TrackedProduct.objects.none()

        # select_related('user') - N+1 muammosidan yiroq turib SQL-so'rovini takomillashtirib beradi
        return TrackedProduct.objects.filter(user=self.request.user).select_related(
            "user"
        )

    def perform_create(self, serializer):
        """
        Avtomatik bog'lanish: joriy foydalanuvchiga
        urg'u berib, majburan mahsulotni saqlaymiz.
        """
        serializer.save(user=self.request.user)

