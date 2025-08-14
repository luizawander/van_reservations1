from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserReservationForm, CustomUserCreationForm
from .models import UserReservation
from datetime import date


@login_required
def make_reservation(request):
    today = date.today()
    reservation = UserReservation.objects.filter(user=request.user, date=today).first()

    if request.method == 'POST':
        form = UserReservationForm(request.POST, instance=reservation, user=request.user)
        if form.is_valid():
            new_reservation = form.save(commit=False)
            new_reservation.user = request.user
            new_reservation.date = today
            new_reservation.save()
            return redirect('make_reservation')
    else:
        form = UserReservationForm(instance=reservation, user=request.user)

    return render(request, 'reservations/reservation_form.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('make_reservation')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = AuthenticationForm()
    return render(request, 'reservations/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Conta criada com sucesso! Faça login.")
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})
