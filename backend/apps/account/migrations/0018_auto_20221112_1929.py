# Generated by Django 3.2.16 on 2022-11-12 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_merge_20221112_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorspecialitymodel',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doc_speciality_branch', to='account.branchmodel'),
        ),
        migrations.AlterField(
            model_name='doctorspecialitymodel',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doc_speciality_org', to='account.organizationmodel'),
        ),
        migrations.AlterField(
            model_name='doctorspecialitymodel',
            name='speciality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doc_speciality_spec', to='account.specialitymodel'),
        ),
    ]