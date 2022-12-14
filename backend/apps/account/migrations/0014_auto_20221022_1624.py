# Generated by Django 3.2.16 on 2022-10-22 11:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_account_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='f_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='l_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='m_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patientmodel',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 22, 11, 24, 9, 817726, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patientmodel',
            name='last_visit_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
