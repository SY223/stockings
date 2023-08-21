# Generated by Django 4.2.1 on 2023-07-26 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockright', '0002_alter_customuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email_address_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
