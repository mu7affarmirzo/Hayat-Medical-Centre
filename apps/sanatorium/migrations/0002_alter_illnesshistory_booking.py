# Generated by Django 5.0.4 on 2024-08-31 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logus', '0011_alter_bookingmodel_stage'),
        ('sanatorium', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='illnesshistory',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logus.bookingmodel'),
        ),
    ]
