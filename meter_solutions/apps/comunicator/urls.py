from django.urls import path

from apps.comunicator.views import turn_off, turn_on

urlpatterns = [
    path('turn_off/<meter_id>', turn_off),
    path('turn_on/<meter_id>', turn_on),
]