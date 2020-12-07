import json

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.meter.api.data_serializer import DataSerializer
from apps.meter.api.device_group_serializer import DeviceGroupListSerializer, DeviceGroupUpdateSerializer, \
    DeviceGroupAddDeviceSerializer
from apps.meter.api.device_model_serializer import DeviceModelSerializer, DeviceTypeSerializer
from apps.meter.api.device_serializer import DeviceUpdateSerializer, DeviceListSerializer
from apps.meter.api.indication_serializer import IndicationSerializer
from apps.meter.models import Data, DeviceModel, DeviceType, Indication
from apps.meter.models.device import Device
from apps.meter.models.device_group import DeviceGroup


class DeviceViewSet(ModelViewSet):

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return DeviceListSerializer
        else:
            return DeviceUpdateSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Device.objects.filter(owner=user)
        return queryset

    @action(detail=True, methods=['get'])
    def get_latest_data(self, request, pk=None):
        device = self.get_object()

        indications = DeviceModel.objects.filter(id=device.device_model_id).last().indications.all()
        result = []
        for indication in indications:
            last_data = Data.objects.filter(device=device).filter(indication=indication).last()
            result.append({'timestamp': str(last_data.timestamp).split(".")[0], 'value': str(last_data.value),
                           'measurement': str(last_data.indication.measurement),
                           'designation': str(last_data.indication.designation)})
        return Response(result)

    @action(detail=True, methods=['get'])
    def get_data_by_date(self, request, pk=None):
        device = self.get_object()

        indication = Indication.objects.filter(measurement=request.GET['measurement']).last()
        result = []
        start_date = request.GET['start-date'].replace('T', ' ')
        end_date = request.GET['end-date'].replace('T', ' ')
        last_data = Data.objects.filter(device=device).filter(indication=indication).filter(timestamp__gte=start_date).filter(timestamp__lte=end_date)
        for data in last_data:
            result.append({'timestamp': str(data.timestamp).split(".")[0], 'value': str(data.value)})
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


class DeviceGroupViewSet(ModelViewSet):

    def get_queryset(self):
        user = self.request.user
        queryset = DeviceGroup.objects.filter(owner=user)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return DeviceGroupListSerializer
        else:
            return DeviceGroupUpdateSerializer

    @action(detail=True, methods=['post'])
    def add_device(self, request, pk=None):
        device_group = self.get_object()

        serializer = DeviceGroupAddDeviceSerializer(data=request.data)

        if serializer.is_valid():
            device_group.add_devices(serializer.data['devices'])
            device_group.save()
            return Response({'status': 'devices added to the group'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
