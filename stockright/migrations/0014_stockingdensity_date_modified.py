# Generated by Django 4.2.1 on 2023-06-17 17:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stockright', '0013_pond_date_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockingdensity',
            name='date_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
