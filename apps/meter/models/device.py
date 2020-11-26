from django.db import models

from apps.meter.models.device_model import DeviceModel

DEVICE_ON = 1
DEVICE_OFF = 2
DEVICE_UNDEFINED = 3
DEVICE_STATUS = (
    (DEVICE_ON, "Включен"),
    (DEVICE_OFF, "Выключен"),
    (DEVICE_UNDEFINED, "Неизвестно"),
)


class Device(models.Model):
    """
        Describes a device and all info about it.

        name - name of device that specified by owner
        owner - user that is owner of device
        status - device status (on / off / undefined)
        device_model - device model
        last_update - timestamp of the last communication with device
        mqtt_id - id that is using for device connection with mqtt broker
    """
    name = models.CharField(max_length=255)
    #owner = models.ForeignKey(on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=DEVICE_STATUS, default=DEVICE_UNDEFINED)
    device_model = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now_add=True)
    mqtt_id = models.CharField(max_length=255)

    def __str__(self):
        return f'Id {self.id}: {self.name}'

