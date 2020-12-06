from rest_framework.routers import SimpleRouter

from apps.meter.views import DeviceViewSet, DeviceModelViewSet, \
    DeviceTypeViewSet, DataViewSet, IndicationViewSet, DeviceGroupViewSet


router = SimpleRouter()

router.register(r'device', DeviceViewSet)
router.register(r'device_model', DeviceModelViewSet)
router.register(r'device_type', DeviceTypeViewSet)
router.register(r'data', DataViewSet)
router.register(r'indication', IndicationViewSet)
router.register(r'device_group', DeviceGroupViewSet)


urlpatterns = router.urls
