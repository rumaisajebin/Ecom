# Generated by Django 4.2.6 on 2023-12-18 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0031_product_d_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='d_price',
        ),
    ]
