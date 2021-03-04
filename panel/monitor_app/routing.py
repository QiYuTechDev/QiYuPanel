from django.urls import path

from . import consumer

__all__ = ["websocket_urlpatterns"]

websocket_urlpatterns = [
    path("ws/monitor/cpu/", consumer.CpuMonitorConsumer.as_asgi()),
]
