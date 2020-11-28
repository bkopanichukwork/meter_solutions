import random
import time

from paho.mqtt import client as mqtt_client

from apps.comunicator.services.handlers import Zmai90Decoder

broker = '15.236.242.30'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 1000)}'
topic = "cmnd/tasmota_5A1C05/POWER"
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


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print('\n' + f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        Zmai90De2coder.decode(msg.payload.decode().split(':')[1][1:-1])

    client.subscribe(topic)
    client.on_message = on_message


def run(args):
    connector = connect_mqtt()
    connector.loop_forever()
    result = connector.publish(topic, "ON")
    status = result[0]
    print(status)