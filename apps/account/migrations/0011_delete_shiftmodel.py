# Generated by Django 5.1.1 on 2025-04-21 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_account_is_therapist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShiftModel',
        ),
    ]
