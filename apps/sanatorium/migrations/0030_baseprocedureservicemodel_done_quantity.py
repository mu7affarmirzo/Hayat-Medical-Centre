# Generated by Django 5.1.1 on 2024-10-18 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanatorium', '0029_proceduredaysmodel_is_out_of_graphic'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseprocedureservicemodel',
            name='done_quantity',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
