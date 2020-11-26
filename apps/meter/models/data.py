from django.db import models

from apps.meter.models.device import Device
from apps.meter.models.indication import Indication


class Data(models.Model):
    """
        device - device id
        indication - type of data indication
        timestamp - moment of data receiving from mqtt_broker
        value - value of the dataframe
    """
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    indication = models.ForeignKey(Indication, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now=True)
    value = models.DecimalField(max_digits=16, decimal_places=4)

