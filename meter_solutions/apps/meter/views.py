from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.meter.api.data_serializer import DataSerializer
from apps.meter.api.device_model_serializer import DeviceModelSerializer, DeviceTypeSerializer
from apps.meter.api.device_serializer import DeviceSerializer
from apps.meter.api.indication_serializer import IndicationSerializer
from apps.meter.models import Data, DeviceModel, DeviceType, Indication
from apps.meter.models.device import Device


class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DataViewSet(ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class DeviceModelViewSet(ModelViewSet):
    queryset = DeviceModel.objects.all()
    serializer_class = DeviceModelSerializer


class DeviceTypeViewSet(ModelViewSet):
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer


class IndicationViewSet(ModelViewSet):
    queryset = Indication.objects.all()
    serializer_class = IndicationSerializer
