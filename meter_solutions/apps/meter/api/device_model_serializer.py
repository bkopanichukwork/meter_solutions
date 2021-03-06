from rest_framework.serializers import ModelSerializer

from apps.meter.api.indication_serializer import IndicationSerializer
from apps.meter.models import Indication
from apps.meter.models.device_model import DeviceModel, DeviceType


class DeviceTypeSerializer(ModelSerializer):
    main_indication = IndicationSerializer(many=False, read_only=True)

    class Meta:
        model = DeviceType
        fields = ['type', 'main_indication']


class DeviceModelSerializer(ModelSerializer):

    indications = IndicationSerializer(many=True, read_only=True)
    type = DeviceTypeSerializer(many=False, read_only=True)

    class Meta:
        model = DeviceModel
        fields = ['name', 'is_switchable', 'indications', 'type']
