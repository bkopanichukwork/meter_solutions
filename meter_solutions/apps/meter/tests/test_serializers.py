from django.test import TestCase

from apps.meter.models.device import Device
from apps.meter.api.data_serializer import DeviceSerializer


class MeterSerializerTestCase(TestCase):
    def test_ok(self):
        meter_1 = Device.objects.create(name='ZMAI-90', price='123.22', author_name="Anton")
        meter_2 = Device.objects.create(name='ZMAI-91', price='123', author_name="Denis")
        data = DeviceSerializer([meter_1, meter_2], many=True).data
        expected_data = [
            {
                'id': meter_1.id,
                'name': 'ZMAI-90',
                'price': '123.22',
                'author_name': 'Anton',
            },
            {
                'id': meter_2.id,
                'name': 'ZMAI-91',
                'price': '123.00',
                'author_name': 'Denis',
            }
        ]
        self.assertEqual(expected_data, data)


