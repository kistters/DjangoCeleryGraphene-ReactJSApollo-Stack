import os

import django
from django.urls import path
from channels import routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adventure.settings')
django.setup(set_prefix=False)

from adventure.schema import MyGraphqlWsConsumer

application = routing.ProtocolTypeRouter({
    'websocket': routing.URLRouter([
        path('ws/graphql/', MyGraphqlWsConsumer),
    ])
})
