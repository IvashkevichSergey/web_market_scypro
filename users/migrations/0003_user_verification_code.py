# Generated by Django 4.2.3 on 2023-08-27 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verification_code',
            field=models.CharField(default='411299', max_length=10),
        ),
    ]
