import json

from django.core import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
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

    @action(detail=True, methods=['get'])
    def get_latest_data(self, request, pk=None):
        device = Device.objects.filter(id=pk).last()
        indications = DeviceModel.objects.filter(id=device.device_model_id).last().indications.all()
        result = []
        for indication in indications:
            last_data = Data.objects.filter(device=device).filter(indication=indication).last()
            result.append({'timestamp': str(last_data.timestamp), 'value': str(last_data.value), 'measurement': str(last_data.indication.measurement), 'designation': str(last_data.indication.designation)})
        return Response(result)


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