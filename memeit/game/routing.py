from django.conf.urls import url
from game.consumers import MemeItConsumer

websocket_urlpatterns = [
    url(r'^ws/play/(?P<room_id>\w+)/$', MemeItConsumer.as_asgi()),
]