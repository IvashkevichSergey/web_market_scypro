# Generated by Django 4.2.3 on 2023-08-04 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_product_changed_at_alter_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='phone_number',
            field=models.TextField(verbose_name='номер'),
        ),
        migrations.AlterField(
            model_name='product',
            name='changed_at',
            field=models.DateField(default=datetime.datetime(2023, 8, 4, 12, 13, 10, 735945, tzinfo=datetime.timezone.utc), verbose_name='дата изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 8, 4, 12, 13, 10, 735945, tzinfo=datetime.timezone.utc), verbose_name='дата создания'),
        ),
    ]
