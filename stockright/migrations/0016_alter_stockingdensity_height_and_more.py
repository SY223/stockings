# Generated by Django 4.2.1 on 2023-06-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockright', '0015_alter_stockingdensity_length_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockingdensity',
            name='height',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stockingdensity',
            name='thirty_percent_decrease',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stockingdensity',
            name='to_stock',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stockingdensity',
            name='twenty_percent_decrease',
            field=models.FloatField(),
        ),
    ]
