# Generated by Django 5.2.4 on 2025-07-28 14:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreservation',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, help_text='Date of the reservation'),
        ),
        migrations.AlterField(
            model_name='userreservation',
            name='hour_going',
            field=models.CharField(blank=True, choices=[('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30')], help_text='Departure time from the office', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='userreservation',
            name='hour_return',
            field=models.CharField(blank=True, choices=[('11:40', '11:40'), ('12:10', '12:10'), ('12:40', '12:40'), ('13:10', '13:10'), ('13:40', '13:40'), ('14:00', '14:00')], help_text='Return time from the restaurant', max_length=5, null=True),
        ),
    ]
