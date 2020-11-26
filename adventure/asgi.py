import os

import django
from django.urls import path
from channels import routing

from adventure.schema import MyGraphqlWsConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adventure.settings')
django.setup(set_prefix=False)

application = routing.ProtocolTypeRouter({
    'websocket': routing.URLRouter([
        path('ws/graphql/', MyGraphqlWsConsumer),
    ])
})
