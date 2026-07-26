from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TrackedProductViewSet

# REST-routerni faollashtirish
router = DefaultRouter()
# ViewSet'imizni 'products' prefiksi bilan ro'yxatdan o'tkazamiz
router.register(r"products", TrackedProductViewSet, basename="tracked-products")

urlpatterns = [
    # Avtomatik ravishda yaratilgan barcha yo'llarni ulaymiz
    path("", include(router.urls)),
]
