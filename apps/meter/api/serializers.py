from rest_framework.serializers import ModelSerializer

from apps.meter.models.device import Device


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
