# Generated by Django 4.2.6 on 2023-11-27 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='average_response_time',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='fulfillment_rate',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='on_time_delivery_rate',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='quality_rating_avg',
        ),
    ]