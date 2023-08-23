from django.utils import timezone
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='media/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория товара')
    price = models.IntegerField(verbose_name='цена')
    created_at = models.DateField(verbose_name='дата создания', default=timezone.now)
    changed_at = models.DateField(verbose_name='дата изменения', default=timezone.now)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('changed_at',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.SmallIntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=50, verbose_name='название версии')
    is_current = models.BooleanField(default=True, verbose_name='актуальная версия?')

    def __str__(self):
        return f'Версия {self.version_number} для продукта {self.product}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'


class Contacts(models.Model):
    phone_number = models.CharField(max_length=20, verbose_name='номер')
    address = models.TextField(verbose_name='адрес')

    def __str__(self):
        return f'Адрес: {self.address}' \
               f'Телефон для связи: {self.phone_number}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, unique=True, verbose_name='псевдоним')
    body = models.TextField(verbose_name='текст блога')
    image = models.ImageField(upload_to='media/', verbose_name='превью', **NULLABLE)
    created_at = models.DateField(verbose_name='дата создания', default=timezone.now)
    is_published = models.BooleanField(default=True, verbose_name='запись опубликована?')
    views = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'Запись "{self.title}"'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('created_at',)
