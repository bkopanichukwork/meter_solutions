"""
    Client that invokes in background every N seconds
    and receives data from subscribed devices.
"""
import os

from apps.comunicator.services.backend.handlers import handlers
from apps.comunicator.services.backend.mqtt_client import MqttClient


def init_receiver():
    client = MqttClient()

    meter_id = "zmai90_5002915A1C05"
    DeviceHandler = handlers.get_device_data_handler("zmai90")
    client.subscribe("zmai90_5002915A1C05/tele/RESULT", DeviceHandler.on_message)
    client.connector.loop_start()
