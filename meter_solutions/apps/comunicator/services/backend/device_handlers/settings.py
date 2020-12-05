import os

BROKER = '15.236.242.30'

PORT = 1883

CLIENT_ID = f'python-mqtt-bogdan_ueban'

MAX_INFLIGHT_MESSAGES = 100

DATABASE_URL = os.getenv('DATABASE_URL')

INDICATION_TABLE = "meter_indication"

DATA_TABLE = "meter_data"

DEVICES_TABLE = "meter_device"