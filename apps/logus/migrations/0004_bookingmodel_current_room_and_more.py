# Generated by Django 5.0.4 on 2024-07-31 20:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_notificationmodel_sender'),
        ('logus', '0003_alter_bookedroommodel_room'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingmodel',
            name='current_room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booking', to='logus.availableroommodel'),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='current_room_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booking_type', to='logus.roomtypemodel'),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='current_tariff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booking_tariff', to='logus.tariffmodel'),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='discount',
            field=models.IntegerField(blank=True, choices=[(0, 0), (5, 5), (10, 10), (15, 15), (20, 20), (25, 25), (30, 30)], default=0, null=True),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='is_checked_out',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='account.patientmodel'),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='stage',
            field=models.CharField(choices=[('booked', 'booked'), ('settled', 'settled'), ('arrived', 'arrived'), ('cancelled', 'cancelled')], default='booked', max_length=10),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='BookingHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('booking', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_history', to='logus.bookingmodel')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booking_history', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modf_booking_history', to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booking_history', to='logus.availableroommodel')),
                ('room_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booking_history_type', to='logus.roomtypemodel')),
                ('tariff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booking_history_tariff', to='logus.tariffmodel')),
            ],
        ),
    ]
