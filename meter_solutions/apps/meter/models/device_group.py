from django.db import models

from apps.authentication.models import User
from apps.meter.models.device import Device
from apps.meter.models.device_model import DeviceModel


class DeviceGroup(models.Model):
    """
        Describes a device group and all info about it.

        name - name of the device group that specified by owner
        owner - user that is owner of the grout
        devices - list of devices that in this group
    """
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    devices = models.ManyToManyField(Device)

    def __str__(self):
        return f'{self.name}'

