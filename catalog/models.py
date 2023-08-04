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
    created_at = models.DateField(verbose_name='дата создания', default=timezone.now())
    changed_at = models.DateField(verbose_name='дата изменения', default=timezone.now())

    def __str__(self):
        return f'{self.title} из категории {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('changed_at',)


class Contacts(models.Model):
    phone_number = models.CharField(max_length=20, verbose_name='номер')
    address = models.TextField(verbose_name='адрес')

    def __str__(self):
        return f'Адрес: {self.address}' \
               f'Телефон для связи: {self.phone_number}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
