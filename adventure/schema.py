import graphene

import adventure.apps.poke.schema as PokeSchema
import adventure.apps.trainer.schema as TrainerSchema

class Query(graphene.ObjectType,
      PokeSchema.Query,
      TrainerSchema.Query):
	"""Adventure Query Class, where is included Schema.Query 
	of the apps 4 enjoyment"""
	pass

class Mutation(graphene.ObjectType):
	"""docstring for Mutation"""
	pass

schema = graphene.Schema(query=Query)
""" https://www.howtographql.com/graphql-python/0-introduction/ """
