# adventure
Adventure Poke using django and graphene.. :)

## Building 
```sh
$ bash adventure-up.sh --build
```

> frontend [ReactJs](http://127.0.0.1:3000/) 

> backend [/graphQL](http://127.0.0.1:8000/graphql/)
 
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
