from django.contrib import admin
from .models import UserReservation
from .forms import UserReservationForm  
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

@admin.register(UserReservation)
class UserReservationAdmin(admin.ModelAdmin):
    form = UserReservationForm  
    list_display = ('user', 'date', 'hour_going', 'hour_return', 'reservation_type', 'created_at')
    list_filter = ('date', 'reservation_type')
    search_fields = ('user__username',)
    fields = ('user', 'date', 'hour_going', 'hour_return', 'reservation_type')

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")



class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'is_staff')


# Re-registra o User com o admin customizado
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)