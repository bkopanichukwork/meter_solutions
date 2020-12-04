from rest_framework.serializers import ModelSerializer

from apps.meter.models.device_model import DeviceModel, DeviceType


class DeviceModelSerializer(ModelSerializer):
    class Meta:
        model = DeviceModel
        fields = '__all__'


class DeviceTypeSerializer(ModelSerializer):
    class Meta:
        model = DeviceType
        fields = '__all__'
