import graphene

import adventure.apps.poke.schema as PokeSchema

class Query(PokeSchema.Query,
			graphene.ObjectType):
	"""Adventure Query Class, where is included Schema.Query 
	of the apps 4 enjoyment"""
	pass

class Mutation(graphene.ObjectType):
	"""docstring for Mutation"""
	pass

schema = graphene.Schema(query=Query)


#test in /graphql
'''
query {
  pokemons:allPokemons {
    name
    id
  },
  types:allTypes {
    name
  },
  pokemonsWithTypesList:allPokemons {
    name,
    types {
      name
    },
  },
  typesWithPokemonList:allTypes {
    name,
    poke_list:pokemonSet {
      name
    }
  },
  pokemonsWithTypesListByName:allPokemons(pokeName:"cha") {
    name,
    types {
      name
    },
  },
  typesWithPokemonListByName:allTypes(typeName:"grass") {
    name,
    poke_list:pokemonSet {
      name
    }
  }
}
'''