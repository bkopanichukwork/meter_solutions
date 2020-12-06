from rest_framework.serializers import ModelSerializer

from apps.meter.models.indication import Indication


class IndicationSerializer(ModelSerializer):
    class Meta:
        model = Indication
        fields = ['measurement', 'designation', ]
