# master routing.py for ASGI

from channels.routing import ProtocolTypeRouter, URLRouter
import messageapp.api.routing

application = ProtocolTypeRouter({
    'http': URLRouter(messageapp.api.routing.urlpatterns),
})
