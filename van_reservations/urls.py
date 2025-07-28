from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from reservations import views, templates


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reservations.urls')),
]
