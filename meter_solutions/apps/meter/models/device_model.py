from django.db import models

from apps.meter.models.indication import Indication


class DeviceType(models.Model):
    """
        Describes a device type (e.g. water, electricity, ...)
        and the main indication of devices with this type
    """
    type = models.CharField(max_length=127)
    main_indication = models.ForeignKey(Indication, on_delete=models.CASCADE)


class DeviceModel(models.Model):
    """
        Describes a device model (e.g. ZMAI-90).

        indication - list of all indications that the system receives from devices of this model
        type - type of device model
        is_switchable - true if a device can be turned of remotely otherwise no

        !this model can be extended by other fields later.
    """
    name = models.CharField(max_length=255)
    type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    indications = models.ManyToManyField(Indication)
    is_switchable = models.BooleanField(default=True)
