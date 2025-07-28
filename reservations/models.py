# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

GOING_HOURS = [
    ("11:00", "11:00"),
    ("11:30", "11:30"),
    ("12:00", "12:00"),
    ("12:30", "12:30"),
    ("13:00", "13:00"),
    ("13:30", "13:30"),
]

RETURN_HOURS = [
    ("11:40", "11:40"),
    ("12:10", "12:10"),
    ("12:40", "12:40"),
    ("13:10", "13:10"),
    ("13:40", "13:40"),
    ("14:00", "14:00"),
]

class UserReservation(models.Model):
    RESERVATION_TYPE_CHOICES = (
        ('GOING', 'Only Going'),
        ('RETURN', 'Only Return'),
        ('BOTH', 'Going and Return'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User who made the reservation"
    )

    date = models.DateField(
        default=timezone.now,
        help_text="Date of the reservation"
    )

    hour_going = models.CharField(
        max_length=5,  
        choices=GOING_HOURS,
        null=True, blank=True,
        help_text="Departure time from the office"
    )

    hour_return = models.CharField(
        max_length=5,
        choices=RETURN_HOURS,
        null=True, blank=True,
        help_text="Return time from the restaurant"
    )

    reservation_type = models.CharField(
        max_length=10,
        choices=RESERVATION_TYPE_CHOICES,
        default='BOTH',
        help_text="Type of reservation: only going, only return, or both"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp of reservation creation"
    )

    def __str__(self):
        return f"{self.user.username} - {self.date} ({self.get_reservation_type_display()})"
