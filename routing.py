from django.urls import re_path
from sample.consumers import SampleConsumer

websocket_urlpatterns = [
    re_path(r'ws/auth/(?P<user_id>\w+)/$', SampleConsumer.as_asgi()),
]
