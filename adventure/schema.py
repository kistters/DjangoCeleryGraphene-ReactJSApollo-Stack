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


#test in /graphql
'''
{
  pokemons: allPokemons {
    name
    id
    catchBy: pokeballSet {
      owner {
        username
      }
    }
  }
  types: allTypes {
    name
  }
  pokemonsWithTypesList: allPokemons {
    name
    types {
      name
    }
  }
  typesWithPokemonList: allTypes {
    name
    poke_list: pokemonSet {
      name
    }
  }
  pokemonsWithTypesListByName: allPokemons(pokeName: "cha") {
    name
    types {
      name
    }
  }
  typesWithPokemonListByName: allTypes(typeName: "grass") {
    name
    poke_list: pokemonSet {
      name
    }
  }
  trainersWithPokeballs: allTrainers {
    username
    email
    pokeballs {
      customName: name
      poke {
        id
        pokeId
      }
    }
  }
  pokeballsWithOwners: allPokeballs {
    id
    customName: name
    owner {
      username
    }
    poke {
      name
      pokeId
    }
  }
  pokeballsAllList:allPokeballs{
    ...PokeBallEntity
  }
}

##Fragments
fragment PokeBallEntity on PokeballType {
  customName: name
  owner {
    id
    username
  }
  poke {
    ...PokeEntity
  }
}

fragment PokeEntity on PokemonType {
  name
  pokeId
  imgDefault
  imgShiny
}
'''