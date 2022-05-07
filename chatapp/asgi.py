import os

import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path

from chat.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp.settings')
django.setup()

application = ProtocolTypeRouter({
  "http": AsgiHandler(),
  # Just HTTP for now. (We can add other protocols later.)

  "websocket": AuthMiddlewareStack(URLRouter([path('ws/chat/<int:room_name>/', ChatConsumer.as_asgi())]))
})




# import os
# import django

# from channels.http import AsgiHandler
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# from django.conf.urls import path

# from chat.consumers import ChatConsumer

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp.settings')

# django_asgi_app = get_asgi_application() #colling first
# from apps.drivers import routing # colling second

# application = ProtocolTypeRouter({
#     "http" : django_asgi_app(),

#     # Just HTTP for now. (We can add other protocols later.)
#     "websocket": URLRouter([path('ws/chat/<int:room_name>/', ChatConsumer.as_asgi())])
# })