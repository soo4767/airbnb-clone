# Generated by Django 2.2.5 on 2021-08-22 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20210822_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='list', to=settings.AUTH_USER_MODEL),
        ),
    ]
