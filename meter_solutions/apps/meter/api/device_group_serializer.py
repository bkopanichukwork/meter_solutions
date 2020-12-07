from rest_framework.serializers import ModelSerializer

from apps.meter.api.device_serializer import DeviceSerializer
from apps.meter.models.device_group import DeviceGroup


class DeviceGroupSerializer(ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=False)

    class Meta:
        model = DeviceGroup
        fields = ['name', 'owner', 'devices']
