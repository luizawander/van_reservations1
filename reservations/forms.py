from django import forms
from .models import UserReservation, GOING_HOURS, RETURN_HOURS
from datetime import date

class UserReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  
        super().__init__(*args, **kwargs)

        if 'user' in self.fields:
            self.fields['user']

        today = date.today()

        if 'date' in self.fields:
            self.fields['date'].initial = today

        if not self.instance.pk and 'date' in self.fields:
            self.fields['date'].initial = today

        available_going = []
        for hour in GOING_HOURS:
            count = UserReservation.objects.filter(date=today, hour_going=hour[0]).count()
            if count < 15 or (self.instance and self.instance.hour_going == hour[0]):
                available_going.append(hour)

        available_return = []
        for hour in RETURN_HOURS:
            count = UserReservation.objects.filter(date=today, hour_return=hour[0]).count()
            if count < 15 or (self.instance and self.instance.hour_return == hour[0]):
                available_return.append(hour)

        self.fields['hour_going'] = forms.ChoiceField(choices=[('', '---')] + available_going, required=False)
        self.fields['hour_return'] = forms.ChoiceField(choices=[('', '---')] + available_return, required=False)

    class Meta:
        model = UserReservation
        fields = ['reservation_type', 'hour_going', 'hour_return']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.date = date.today()  # força a data como hoje
        if commit:
            instance.save()
        return instance
