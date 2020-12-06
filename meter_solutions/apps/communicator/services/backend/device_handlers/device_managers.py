from abc import abstractmethod


class BaseDeviceManager:

    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client

    @abstractmethod
    def turn_on(self, device_id):
        pass

    @abstractmethod
    def turn_off(self, device_id):
        pass

    @abstractmethod
    def send_message(self, device_id, topic, message):
        pass


class Zmai90DeviceManager(BaseDeviceManager):

    power_topic = "/cmnd/POWER"

    def turn_on(self, device_id):
        topic = device_id + Zmai90DeviceManager.power_topic
        self.mqtt_client.publish(topic, "ON")

    def turn_off(self, device_id):
        topic = device_id + Zmai90DeviceManager.power_topic
        self.mqtt_client.publish(topic, "OFF")

    def send_message(self, device_id, topic, message):
        topic = device_id + topic
        self.mqtt_client.publish(topic, message)
