"""
    Client that invokes in background every N seconds
    and receives data from subscribed devices.
"""
from apps.comunicator.services.backend.handlers import handlers
from apps.comunicator.services.backend.mqtt_client import MqttClient


def receive():
    client = MqttClient()

    meter_id = "zmai90_5002915A1C05"

    DeviceHandler = handlers.get_device_data_handler("zmai90")
    handler = DeviceHandler()
    client.subscribe("zmai90_5002915A1C05/tele/RESULT", handler.on_message)
    client.connector.loop_start()
