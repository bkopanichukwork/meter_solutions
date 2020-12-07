from rest_framework.permissions import IsAdminUser
from rest_framework.serializers import ModelSerializer

from apps.meter.api.device_model_serializer import DeviceModelSerializer
from apps.meter.api.permissions import IsOwner
from apps.meter.models.device import Device


class DeviceListSerializer(ModelSerializer):
    device_model = DeviceModelSerializer(many=False, read_only=True)
    permission_classes = [IsOwner, IsAdminUser]

    class Meta:
        model = Device
        fields = ['id',
                  'name',
                  'owner',
                  'status',
                  'last_update',
                  'mqtt_id',
                  'device_model']


class DeviceUpdateSerializer(ModelSerializer):
    permission_classes = [IsOwner, IsAdminUser]

    class Meta:
        model = Device
        fields = ['id',
                  'name',
                  'status',
                  'last_update',
                  'mqtt_id',
                  'device_model']

    def perform_create(self, serializer):
        self.validated_data['owner'] = self.request.user
        serializer.save()
