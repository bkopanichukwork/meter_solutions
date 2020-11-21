from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from meter.models import Meter
from meter.serializers import MeterSerializer


class MeterApiTestCase(APITestCase):
    def setUp(self):
        self.meter_1 = Meter.objects.create(name='ZMAI-90', price='123.22', author_name="Anton")
        self.meter_2 = Meter.objects.create(name='ZMAI-91', price='123', author_name="Denis")
        self.meter_3 = Meter.objects.create(name='Denis-91', price='123', author_name="Bogdan")
        pass

    def test_get(self):
        serializer_data = MeterSerializer([self.meter_1, self.meter_2, self.meter_3], many=True).data

        url = reverse('meter-list')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        serializer_data = MeterSerializer([self.meter_2, self.meter_3], many=True).data

        url = reverse('meter-list')
        response = self.client.get(url, data={'price': 123})
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        serializer_data = MeterSerializer([self.meter_2, self.meter_3], many=True).data

        url = reverse('meter-list')
        response = self.client.get(url, data={'search': "Denis"})
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
