# Generated by Django 4.2.6 on 2023-11-30 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0023_coupon_is_expired_alter_coupon_coupon_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='coupon_code',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
