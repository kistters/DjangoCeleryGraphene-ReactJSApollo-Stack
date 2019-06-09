import graphene
import graphql_jwt

from .apps.poke import schema as PokeSchema
from .apps.trainer import schema as TrainerSchema


class Query(graphene.ObjectType, PokeSchema.Query, TrainerSchema.Query):
	"""Adventure Query Class, where is included
	Schema.Query of the apps 4 enjoyment"""
	pass


class Mutation(graphene.ObjectType, TrainerSchema.Mutation):
	"""docstring for Mutation"""
	token_auth = graphql_jwt.ObtainJSONWebToken.Field()
	verify_token = graphql_jwt.Verify.Field()
	refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
""" https://www.howtographql.com/graphql-python/0-introduction/ """
