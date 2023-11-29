# Generated by Django 4.2.6 on 2023-11-29 06:18

from django.db import migrations, models
import v1.orders.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_rename_delivery_date_order_expected_delivery_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.JSONField(blank=True, default=v1.orders.models.Order.default_items, null=True),
        ),
    ]
