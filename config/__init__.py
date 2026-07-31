from .celery import app as celery_app
# Bu Django ishga tushirilganda Celery ilovasi obyektining yuklanishini ta'minlaydi
__all__ = ('celery_app',)