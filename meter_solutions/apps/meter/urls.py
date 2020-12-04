from rest_framework.routers import SimpleRouter

from apps.meter.views import DeviceViewSet, DeviceModelViewSet, \
                             DeviceTypeViewSet, DataViewSet, IndicationViewSet

router = SimpleRouter()

router.register(r'device', DeviceViewSet)
router.register(r'device_model', DeviceModelViewSet)
router.register(r'device_type', DeviceTypeViewSet)
router.register(r'data', DataViewSet)
router.register(r'indication', IndicationViewSet)

urlpatterns = router.urls
