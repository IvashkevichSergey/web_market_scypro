# Generated by Django 4.2.3 on 2023-08-04 12:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_contacts_options_alter_product_changed_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='changed_at',
            field=models.DateField(default=datetime.datetime(2023, 8, 4, 12, 9, 8, 916273, tzinfo=datetime.timezone.utc), verbose_name='дата изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 8, 4, 12, 9, 8, 916273, tzinfo=datetime.timezone.utc), verbose_name='дата создания'),
        ),
    ]
