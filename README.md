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
  pokesWithTypes: allPokemons {
    edges {
      node {
        ...PokeWithTypesEntity
      }
    }
  }
  typesWithPokes: allTypes {
    edges {
      node {
        ...TypesWithPokeEntity
      }
    }
  }
}

fragment TypeEntity on TypeType {
  name
}

fragment PokeEntity on PokemonType {
  name
  pokeId
  imgDefault
  imgShiny
}

fragment TypesWithPokeEntity on TypeType {
  name
  poke_list: pokemonSet {
    edges {
      node {
        ...PokeEntity
      }
    }
  }
}

fragment PokeWithTypesEntity on PokemonType {
  name
  pokeId
  imgDefault
  imgShiny
  types {
    edges {
      node {
        ...TypeEntity
      }
    }
  }
}
```
