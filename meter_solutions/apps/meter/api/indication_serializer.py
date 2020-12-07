from rest_framework.serializers import ModelSerializer

from apps.meter.api.permissions import IsAuthenticatedAndReadOnly
from apps.meter.models.indication import Indication


class IndicationSerializer(ModelSerializer):
    permission_classes = [IsAuthenticatedAndReadOnly, IsAdminUser]

    class Meta:
        model = Indication
        fields = ['id', 'measurement', 'designation', ]
