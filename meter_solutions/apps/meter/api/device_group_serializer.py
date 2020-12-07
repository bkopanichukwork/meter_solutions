from rest_framework.serializers import ModelSerializer

from apps.meter.api.device_serializer import DeviceSerializer
from apps.meter.models.device_group import DeviceGroup


class DeviceGroupListSerializer(ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=True)

    class Meta:
        model = DeviceGroup
        fields = ['name', 'owner', 'devices']


class DeviceGroupUpdateSerializer(ModelSerializer):

    class Meta:
        model = DeviceGroup
        fields = ['name', 'owner', 'devices']

    def create(self, validated_data):
        devices = validated_data.pop('devices')
        album = DeviceGroup.objects.create(**validated_data)
        for device in devices:
            album.devices.add(device)
        return album
