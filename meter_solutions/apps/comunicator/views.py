from django.shortcuts import redirect

# Create your views here.
from apps.comunicator.services import handlers
from apps.comunicator.services.mqtt_client import MqttClient


def turn_off(request, meter_id):
    client = MqttClient()
    DeviceManager = handlers.get_device_manager("zmai90")
    manager = DeviceManager(client)
    manager.turn_off(meter_id)
    client.connector.disconnect()
    return redirect('/')


def turn_on(request, meter_id):
    client = MqttClient()
    DeviceManager = handlers.get_device_manager("zmai90")
    manager = DeviceManager(client)
    manager.turn_on(meter_id)
    client.connector.disconnect()
    return redirect('/')