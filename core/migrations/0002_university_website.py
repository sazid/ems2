# Generated by Django 3.0 on 2019-12-28 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='website',
            field=models.URLField(blank=True, default=''),
        ),
    ]
