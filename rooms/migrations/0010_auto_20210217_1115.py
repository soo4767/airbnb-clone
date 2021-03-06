# Generated by Django 2.2.5 on 2021-02-17 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0009_auto_20210217_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='room_photos'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms', to='rooms.RoomType'),
        ),
    ]
