from apps.communicator.services.backend.device_handlers import handlers
from apps.communicator.services.backend.mqtt_client import MqttClient


def get_device_model_by_id(device_id):
    return device_id.split('_')[0]


def get_device_manager_by_id(device_id, client):
    model = get_device_model_by_id(device_id)
    DeviceManager = handlers.get_device_manager(model)
    return DeviceManager(client)


def toggle(device_id: str, turn_on: bool):
    client = MqttClient()
    manager = get_device_manager_by_id(device_id, client)

    if turn_on:
        manager.turn_off(device_id)
    else:
        manager.turn_off(device_id)

    client.disconnect()


def turn_on(device_id: str):
    toggle(device_id, True)


def turn_off(device_id: str):
    toggle(device_id, False)

