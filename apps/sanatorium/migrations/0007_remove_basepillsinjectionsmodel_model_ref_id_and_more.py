# Generated by Django 5.0.4 on 2024-09-22 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sanatorium', '0006_remove_initialappointmentwithdoctormodel_ill_part_stomach_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basepillsinjectionsmodel',
            name='model_ref_id',
        ),
        migrations.RemoveField(
            model_name='basepillsinjectionsmodel',
            name='model_type',
        ),
    ]
