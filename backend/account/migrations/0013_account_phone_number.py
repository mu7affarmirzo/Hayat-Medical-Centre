# Generated by Django 3.2 on 2022-10-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_specialitymodel_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
