from django.core.cache import cache

from catalog.models import Category
from config import settings


def cache_category():
    """Сервисная функция для кеширования списка категорий товаров"""
    if settings.ALLOW_CACHE:
        key = 'cache_category'
        categories = cache.get(key)
        if categories is None:
            categories = Category.objects.all()
            cache.set(key, categories)
    else:
        categories = Category.objects.all()
    return categories
