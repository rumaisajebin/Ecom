# Generated by Django 4.2.6 on 2023-11-03 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0005_alter_category_options_remove_product_discount_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img1',
            field=models.ImageField(upload_to='product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img2',
            field=models.ImageField(upload_to='product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img3',
            field=models.ImageField(upload_to='product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img4',
            field=models.ImageField(upload_to='product'),
        ),
    ]