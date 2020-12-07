from rest_framework.permissions import IsAdminUser
from rest_framework.serializers import ModelSerializer

from apps.meter.api.device_serializer import DeviceSerializer
from apps.meter.api.permissions import IsOwner
from apps.meter.models.device_group import DeviceGroup


class DeviceGroupListSerializer(ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=True)

    permission_classes = [IsOwner, IsAdminUser]

    read_only_fields = ['id']

    class Meta:
        model = DeviceGroup
        fields = ['id', 'name', 'owner', 'devices']


class DeviceGroupUpdateSerializer(ModelSerializer):
    read_only_fields = ['id']

    permission_classes = [IsOwner, IsAdminUser]

    class Meta:
        model = DeviceGroup
        fields = ['id', 'name', 'devices']

    def create(self, validated_data):
        devices = validated_data.get('devices', None)

        album = DeviceGroup.objects.create(**validated_data, owner=self.context['request'].user)

        if devices:
            for device in devices:
                album.devices.add(device)

        return album
