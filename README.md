# adventure
Adventure Poke using django and graphene.. :)

## Building
```sh
$ git clone https://github.com/kistters/adventure.git
$ cd adventure
$ python3 -m venv venv
$ source venv/bin/activate
$ python migrate
## Gotta catch 'em all
$ python manage.py asyncatchall
$ python manage.py runserver
```
go to [/graphQL](http://127.0.0.1:8000/graphql/) and
try it :)
```graphql
# https://graphql.org/learn/queries/
{
  pokemons: allPokemons {
    name
    pokeId
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
```
