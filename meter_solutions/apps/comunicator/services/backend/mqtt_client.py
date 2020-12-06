from loguru import logger
from paho.mqtt import client as mqtt_client

from apps.comunicator.services.backend import settings


class MqttClient:
    """
        Basic MqttClient
    """

    def __init__(self):
        # Set Connecting Client ID
        self._connector = mqtt_client.Client(client_id=settings.CLIENT_ID, clean_session=False, userdata=None)
        self._connector.on_connect = MqttClient.__on_connect
        self._connector.max_inflight_messages_set(settings.MAX_INFLIGHT_MESSAGES)
        self._connector.connect(settings.BROKER, settings.PORT)

    @staticmethod
    def __on_connect(client_id, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    @staticmethod
    def __on_message(client, userdata, msg):
        print('\n' + f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    def subscribe(self, topic, on_message=None):
        logger.info(f"Subscribed to {topic} topic with {on_message} reaction")
        self._connector.subscribe(topic)

        if not on_message:
            on_message = MqttClient.__on_message

        self._connector.on_message = on_message

    def disconnect(self):
        self._connector.disconnect()

    def start_loop(self):
        self._connector.loop_start()

    def publish(self, topic, message):
        self._connector.publish(topic, message)