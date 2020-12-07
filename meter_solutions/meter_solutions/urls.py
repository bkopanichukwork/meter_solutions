"""
    meter_solutions URL Configuration
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken import views

from .yasg import urlpatterns as doc_urls
from apps.authentication.views import RegistrationAPIView, LoginAPIView

from apps.authentication.views import UserAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.meter.urls')),
    path('communicator/', include('apps.communicator.urls')),
    path('api-token-auth/', views.obtain_auth_token, name="api-token-auth"),
    re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
    re_path(r'^get_user_by_mail/?$', UserAPIView.as_view(), name='get_user_by_mail'),
]

urlpatterns += doc_urls

