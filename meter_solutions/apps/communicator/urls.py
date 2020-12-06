from django.urls import path

from apps.communicator.views import turn_on_view, turn_off_view

urlpatterns = [
    path('turn_off/<device_id>', turn_off_view),
    path('turn_on/<device_id>', turn_on_view),
]