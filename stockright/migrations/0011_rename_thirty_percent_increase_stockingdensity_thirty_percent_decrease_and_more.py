# Generated by Django 4.2.1 on 2023-06-05 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockright', '0010_stockingdensity_thirty_percent_increase_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockingdensity',
            old_name='thirty_percent_increase',
            new_name='thirty_percent_decrease',
        ),
        migrations.RenameField(
            model_name='stockingdensity',
            old_name='twenty_percent_increase',
            new_name='twenty_percent_decrease',
        ),
    ]
