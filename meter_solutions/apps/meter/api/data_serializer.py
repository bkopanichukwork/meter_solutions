from rest_framework.serializers import ModelSerializer

from apps.meter.models.data import Data


class DataSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'
