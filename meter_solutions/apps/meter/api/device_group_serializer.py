from rest_framework.serializers import ModelSerializer

from apps.meter.api.device_serializer import DeviceSerializer
from apps.meter.models.device_group import DeviceGroup


class DeviceGroupSerializer(ModelSerializer):
    devices = DeviceSerializer(many=False, read_only=True)

    class Meta:
        model = DeviceGroup
        fields = ['name', 'devices']
