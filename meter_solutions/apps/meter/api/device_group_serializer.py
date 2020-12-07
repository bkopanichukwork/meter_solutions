from rest_framework.serializers import ModelSerializer

from apps.meter.api.device_serializer import DeviceSerializer
from apps.meter.models.device_group import DeviceGroup


class DeviceGroupListSerializer(ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=True)

    read_only_fields = ['id']

    class Meta:
        model = DeviceGroup
        fields = ['id', 'name', 'owner', 'devices']



class DeviceGroupUpdateSerializer(ModelSerializer):
    read_only_fields = ['id']

    class Meta:
        model = DeviceGroup
        fields = ['id', 'name', 'owner', 'devices']

    def create(self, validated_data):
        devices = validated_data.pop('devices')
        album = DeviceGroup.objects.create(**validated_data)
        for device in devices:
            album.devices.add(device)
        return album
