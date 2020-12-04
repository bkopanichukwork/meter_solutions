from django.shortcuts import render, redirect

# Create your views here.
from apps.comunicator.services.handlers import handlers
from apps.comunicator.services.mqtt_client import MqttClient


def turn_off(request, meter_id):
    client = MqttClient()
    DeviceManager = handlers.get_device_manager("zmai90")
    manager = DeviceManager(client)
    manager.turn_off(meter_id)
    return redirect('/')


def turn_on(request, meter_id):
    client = MqttClient()
    DeviceManager = handlers.get_device_manager("zmai90")
    manager = DeviceManager(client)
    manager.turn_on(meter_id)
    return redirect('/')