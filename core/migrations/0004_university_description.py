# Generated by Django 3.0 on 2019-12-28 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_delete_mcqchoices'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]