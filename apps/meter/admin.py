from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.meter.models import Device


@admin.register(Device)
class DeviceAdmin(ModelAdmin):
    pass
