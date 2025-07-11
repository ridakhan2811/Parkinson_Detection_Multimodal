from django.urls import re_path
from .consumers import PoseConsumer

websocket_urlpatterns = [
    re_path(r'ws/pose/$', PoseConsumer.as_asgi()),
]
