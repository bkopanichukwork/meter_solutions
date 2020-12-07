from rest_framework.serializers import ModelSerializer

from apps.meter.api.device_serializer import DeviceSerializer
from apps.meter.api.permissions import IsOwner
from apps.meter.models.device_group import DeviceGroup


class DeviceGroupListSerializer(ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=True)

    permission_classes = [IsOwner]

    read_only_fields = ['id']

    class Meta:
        model = DeviceGroup
        fields = ['id', 'name', 'owner', 'devices']


class DeviceGroupUpdateSerializer(ModelSerializer):
    read_only_fields = ['id']

    permission_classes = [IsOwner]

    class Meta:
        model = DeviceGroup
        fields = ['id', 'name', 'devices']

    def create(self, validated_data):
        devices = validated_data.pop('devices')
        album = DeviceGroup.objects.create(**validated_data)
        for device in devices:
            album.devices.add(device)
        return album

    def perform_create(self, serializer):
        self.validated_data['owner'] = self.request.user
        serializer.save()
