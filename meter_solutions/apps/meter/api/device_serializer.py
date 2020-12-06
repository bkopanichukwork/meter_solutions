from rest_framework.serializers import ModelSerializer

from apps.meter.api.device_model_serializer import DeviceModelSerializer
from apps.meter.models.device import Device


class DeviceSerializer(ModelSerializer):
    device_model = DeviceModelSerializer(many=False, read_only=True)

    class Meta:
        model = Device
        fields = ['name', 'status', 'last_update', 'mqtt_id', 'device_model']
