import os
from celery import Celery

# 'DJANGO_SETTINGS_MODULE' muhit o'zgaruvchisi uchun Django standart sozlamalarini o'rnatish
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Celery nusxasini loyihamiz nomi bilan ishga tushiramiz
app = Celery('config')


# Celery'ni settings.py'da bo'lgan konfiguratsiyani o'qishga sozlaymiz.
# 'CELERY' prefiksi settings.py ichidagi barcha Celery sozlamalari ushbu harflar bilan boshlanishini bildiradi.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Barcha ro'yxatdan o'tgan (INSTALLED_APPS) ilovalar ichidan fondagi vazifalarni (tasks.py) avtomatik qidiramiz
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    """Vorkerning ishlash qobiliyatini tekshirish uchun sinov-debagger vazifasi"""
    print(f'Celery ishlayapti! So\'rov: {self.request!r}')
