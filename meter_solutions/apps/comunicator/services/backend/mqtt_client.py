from paho.mqtt import client as mqtt_client

from apps.comunicator.services.handlers import settings, handlers


class MqttClient:
    def __init__(self):

        # Set Connecting Client ID
        self.connector = mqtt_client.Client(client_id=settings.CLIENT_ID, clean_session=False, userdata=None)
        self.connector.on_connect = MqttClient.__on_connect
        self.connector.max_inflight_messages_set(settings.MAX_INFLIGHT_MESSAGES)
        self.connector.connect(settings.BROKER, settings.PORT)

    @staticmethod
    def __on_connect(client_id, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    @staticmethod
    def __on_message(client, userdata, msg):
        print('\n' + f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        # Zmai90Decoder.decode(msg.payload.decode().split(':')[1][1:-1])

    def subscribe(self, topic):
        self.connector.subscribe(topic)
        self.connector.on_message = MqttClient.__on_message


def run():
    client = MqttClient()
    DeviceManager = handlers.get_device_manager("zmai90")
    manager = DeviceManager(client)
    manager.turn_off("zmai90_5002915A1C05")
    #client.loop_forever()
    # topic = "zmai90_5002915A1C05/cmnd/POWER"
    # result = client.connector.publish(topic, "ON")


    #connector.loop_forever()



#
# module = import("data_handlers")
#
# handler_name = data_handlers[device_model]
# handler_class = getattr(module, handler_name)
# handler = handler_class()
# handler.decode(message)


if __name__ == "__main__":
    run()
