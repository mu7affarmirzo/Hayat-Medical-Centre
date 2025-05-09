# Generated by Django 5.0.4 on 2024-08-03 09:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logus', '0008_tariffroomtypematrixmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariffroomtypematrixmodel',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='tariffroomtypematrixmodel',
            name='room_type',
        ),
        migrations.AddField(
            model_name='tariffroomtypematrixmodel',
            name='room_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matrix', to='logus.availableroomstypemodel'),
        ),
    ]
