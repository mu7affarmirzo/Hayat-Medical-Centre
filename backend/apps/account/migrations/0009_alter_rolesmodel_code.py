# Generated by Django 3.2 on 2022-10-16 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20220926_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolesmodel',
            name='code',
            field=models.IntegerField(unique=True),
        ),
    ]
