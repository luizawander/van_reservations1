from django import forms
from .models import UserReservation, GOING_HOURS, RETURN_HOURS

class UserReservationForm(forms.ModelForm):
    hour_going = forms.ChoiceField(
        choices=[('', '---')] + GOING_HOURS,
        required=False
    )
    hour_return = forms.ChoiceField(
        choices=[('', '---')] + RETURN_HOURS,
        required=False
    )

    class Meta:
        model = UserReservation
        fields = ['user', 'date', 'hour_going', 'hour_return', 'reservation_type']
