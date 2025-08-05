from django.contrib import admin
from .models import UserReservation
from .forms import UserReservationForm  

@admin.register(UserReservation)
class UserReservationAdmin(admin.ModelAdmin):
    form = UserReservationForm  
    list_display = ('user', 'date', 'hour_going', 'hour_return', 'reservation_type', 'created_at')
    list_filter = ('date', 'reservation_type')
    search_fields = ('user__username',)
    fields = ('user', 'date', 'hour_going', 'hour_return', 'reservation_type')
