from rest_framework.routers import SimpleRouter

from apps.meter.views import DeviceViewSet, DeviceModelViewSet, \
    DeviceTypeViewSet, DataViewSet, IndicationViewSet, DeviceGroupViewSet


router = SimpleRouter()

router.register(r'device', DeviceViewSet, basename='devices')
router.register(r'device_model', DeviceModelViewSet, basename='device_models')
router.register(r'device_type', DeviceTypeViewSet, basename='device_types')
router.register(r'data', DataViewSet, basename='data')
router.register(r'indication', IndicationViewSet, basename='indications')
router.register(r'device_group', DeviceGroupViewSet, basename='device_groups')


urlpatterns = router.urls
