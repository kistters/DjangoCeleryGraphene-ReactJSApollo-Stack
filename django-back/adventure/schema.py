import graphene
import graphql_jwt

from .pokemons import schema as PokeSchema


class Query(graphene.ObjectType, PokeSchema.Query):
    """Adventure Query Class, where is included
    Schema.Query of the apps 4 enjoyment"""
    pass


class Mutation(graphene.ObjectType, PokeSchema.Mutation):
    """docstring for Mutation"""
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class Subscription(graphene.ObjectType, PokeSchema.Subscription):
    """Root GraphQL subscription."""
    pass


schema = graphene.Schema(query=Query, mutation=Mutation, subscription=Subscription)
""" https://www.howtographql.com/graphql-python/0-introduction/ """

"""weird configuration"""

import channels_graphql_ws


class MyGraphqlWsConsumer(channels_graphql_ws.GraphqlWsConsumer):
    """Channels WebSocket consumer which provides GraphQL API."""
    schema = schema

    # Uncomment to send keepalive message every 42 seconds.
    # send_keepalive_every = 42

    # Uncomment to process requests sequentially (useful for tests).
    # strict_ordering = True

    async def on_connect(self, payload):
        """New client connection handler."""
        # You can `raise` from here to reject the connection.
        print("New client connected!")
