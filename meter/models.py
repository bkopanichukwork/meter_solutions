from django.db import models


class Device(models.Model):
    DEVICE_ON = 1
    DEVICE_OFF = 2
    DEVICE_UNDEFINED = 3
    DEVICE_STATUS = (
        (DEVICE_ON, "Включен"),
        (DEVICE_OFF, "Выключен"),
        (DEVICE_UNDEFINED, "Неизвестно"),
    )

    name = models.CharField(max_length=255)
    ###owner = models.ForeignKey(on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=DEVICE_STATUS, default=DEVICE_UNDEFINED)
    #device_model = models.ForeignKey(on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now_add=True)
    device_connection_id = models.CharField(max_length=255)

    def __str__(self):
        return f'Id {self.id}: {self.name}'

