import random
import time

from paho.mqtt import client as mqtt_client

from handlers import handlers

broker = '15.236.242.30'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 1000)}'

connector_id = "123456789"


def connect_mqtt():

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    # Set Connecting Client ID
    connector = mqtt_client.Client(client_id=connector_id, clean_session=False, userdata=None)
    connector.on_connect = on_connect
    connector.max_inflight_messages_set(100)
    connector.connect(broker, port)
    return connector


def subscribe(client: mqtt_client, topic):
    def on_message(client, userdata, msg):
        print('\n' + f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        #Zmai90Decoder.decode(msg.payload.decode().split(':')[1][1:-1])
    print("here")
    client.subscribe(topic)
    print(client.__dict__)
    client.on_message = on_message


def run():
    connector = connect_mqtt()
    DeviceManager = handlers.get_device_manager("zmai90")
    manager = DeviceManager(connector)
    manager.turn_on("zmai90_5002915A1C05")
    connector.loop_forever()
    topic = "zmai90_5002915A1C05/cmnd/POWER"
    result = connector.publish(topic, "ON")


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
