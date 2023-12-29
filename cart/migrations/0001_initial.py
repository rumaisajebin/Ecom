# Generated by Django 4.2.6 on 2023-11-14 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_side', '0009_remove_product_thumbnail'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=200)),
                ('paid_amount', models.IntegerField(default=0)),
                ('is_paid', models.BooleanField(default=False)),
                ('mercahant_id', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='admin_side.product')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.order')),
            ],
        ),
    ]