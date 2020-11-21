from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from meter.models import Device
from meter.serializers import DeviceSerializer


class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]
