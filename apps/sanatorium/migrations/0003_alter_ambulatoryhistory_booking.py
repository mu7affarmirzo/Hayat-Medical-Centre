# Generated by Django 5.0.4 on 2024-08-31 11:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logus', '0011_alter_bookingmodel_stage'),
        ('sanatorium', '0002_alter_illnesshistory_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulatoryhistory',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logus.bookingmodel'),
        ),
    ]
