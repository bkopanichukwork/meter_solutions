from django.shortcuts import redirect

# Create your views here.
from apps.comunicator.services.backend import handlers
from apps.comunicator.services.backend.mqtt_client import MqttClient
from apps.comunicator.services.toggle import turn_off, turn_on


def turn_off_view(request, device_id):
    turn_off(device_id)
    return redirect('/')


def turn_on_view(request, device_id):
    turn_on(device_id)
    return redirect('/')