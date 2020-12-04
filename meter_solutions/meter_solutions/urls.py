"""
    meter_solutions URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.meter.urls')),
    path('comunicator/', include('apps.comunicator.urls')),
]

urlpatterns += doc_urls

