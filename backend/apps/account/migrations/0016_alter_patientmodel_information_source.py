# Generated by Django 3.2.16 on 2022-11-12 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_account_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientmodel',
            name='information_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.informationsourcemodel'),
        ),
    ]