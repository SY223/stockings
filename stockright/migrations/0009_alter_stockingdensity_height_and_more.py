# Generated by Django 4.2.1 on 2023-06-03 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockright', '0008_alter_stockingdensity_height_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockingdensity',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockingdensity',
            name='length',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockingdensity',
            name='width',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
