# Generated by Django 5.0.4 on 2024-07-31 21:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logus', '0004_bookingmodel_current_room_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingmodel',
            name='current_room_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booking_type', to='logus.availableroomstypemodel'),
        ),
    ]
