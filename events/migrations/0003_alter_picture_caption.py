# Generated by Django 4.2.5 on 2023-10-05 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_picture_delete_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='caption',
            field=models.CharField(default='The Redlights', max_length=120),
        ),
    ]