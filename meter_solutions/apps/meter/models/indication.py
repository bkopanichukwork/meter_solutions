from django.db import models


class Indication(models.Model):
    """
        measurement - name of indication (e.g Voltage)
        designation - symbol of indication(e.g. A, kW/h, ...)
    """
    measurement = models.CharField(max_length=64)
    designation = models.CharField(max_length=5)
