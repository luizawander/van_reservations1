from django import forms
from .models import UserReservation, GOING_HOURS, RETURN_HOURS
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import date, datetime


class UserReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  
        super().__init__(*args, **kwargs)

        today = date.today()

        if 'date' in self.fields:
            self.fields['date'].initial = today

        if not self.instance.pk and 'date' in self.fields:
            self.fields['date'].initial = today

        hour_going_value = None
        if 'data' in kwargs:
            raw_hour = kwargs['data'].get('hour_going')
            if raw_hour:
                try:
                    hour_going_value = datetime.strptime(raw_hour, '%H:%M').time()
                except ValueError:
                    pass 
        elif self.instance and self.instance.hour_going:
            hour_going_value = self.instance.hour_going

        available_going = [
            hour for hour in GOING_HOURS
            if UserReservation.objects.filter(date=today, hour_going=hour[0]).count() < 15
            or (self.instance and self.instance.hour_going == hour[0])
        ]

        available_return = [
            hour for hour in RETURN_HOURS
            if UserReservation.objects.filter(date=today, hour_return=hour[0]).count() < 15
            or (self.instance and self.instance.hour_return == hour[0])
        ]

        self.fields['hour_going'] = forms.ChoiceField(choices=[('', '---')] + available_going, required=False)
        self.fields['hour_return'] = forms.ChoiceField(choices=[('', '---')] + available_return, required=False)

    class Meta:
        model = UserReservation
        fields = ['reservation_type', 'hour_going', 'hour_return']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.date = date.today()  
        if commit:
            instance.save()
        return instance

    def clean(self):
        cleaned_data = super().clean()
        hour_going = cleaned_data.get('hour_going')
        hour_return = cleaned_data.get('hour_return')

        if hour_going and hour_return:
            try:
                going_time = datetime.strptime(hour_going, '%H:%M')
                return_time = datetime.strptime(hour_return, '%H:%M')

                if return_time <= going_time:
                    raise forms.ValidationError("O horário de volta deve ser posterior ao horário de ida.")
            except ValueError:
                pass
    

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="E-mail")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Já existe um usuário com este e-mail.")
        return email