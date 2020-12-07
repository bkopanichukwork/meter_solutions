"""
    Client that invokes in background every N seconds
    and receives data from subscribed devices.
"""
from loguru import logger

from apps.communicator.services.backend.db_engine import get_mqtt_ids_list
from apps.communicator.services.backend.device_handlers import handlers, DeviceHandlerNotFound
from apps.communicator.services.backend.mqtt_client import MqttClient


def subscribe_on_devices(client):
    ids = get_mqtt_ids_list()

    for mqtt_id in ids:
        device_model = mqtt_id.split('_')[0]
        try:
            DeviceHandler = handlers.get_device_data_handler(device_model)
        except DeviceHandlerNotFound:
            logger.error("DeviceHandlerNotFound error")
            logger.error(f"skipping {mqtt_id} device")
        else:
            topic_list = DeviceHandler.topics
            for topic_name in topic_list:
                topic = mqtt_id + topic_name
                client.subscribe(topic, DeviceHandler.on_message)
                logger.error(f"Client {client} subscribed on {topic}")


def init_receiver():
    client = MqttClient()
    subscribe_on_devices(client)

    client.start_loop()


def background_receive():
    init_receiver()

    while True:
        pass


