from datetime import datetime
from time import time

from apscheduler.schedulers.blocking import BlockingScheduler

from apps.comunicator.services.handlers import handlers
from apps.comunicator.services.mqtt_client import MqttClient

sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=5)
def timed_job():
    client = MqttClient()
    DeviceManager = handlers.get_device_manager("zmai90")
    manager = DeviceManager(client)
    meter_id = "zmai90_5002915A1C05"


    manager.turn_on(meter_id)
    print('turn_on.')

    client.connector.disconnect()



sched.start()
print("Scheduler started")
