# Generated by Django 4.2.6 on 2023-11-20 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_remove_address_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone_1',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone_2',
            field=models.CharField(blank=True, null=True),
        ),
    ]
