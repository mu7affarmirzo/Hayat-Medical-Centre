# Generated by Django 5.0.4 on 2024-06-22 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0011_itemsinstockmodel_income_registry'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='itemsinstockmodel',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='incomeitemsmodel',
            name='expire_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='itemsinstockmodel',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
