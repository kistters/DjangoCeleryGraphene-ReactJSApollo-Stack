import React from 'react'
//import { Link } from 'react-router-dom'
import { graphql } from 'react-apollo'
import gql from 'graphql-tag'
import Poke from '../components/Poke'

class ListPoke extends React.Component {

  render() {

    if (this.props.allPokemonsQuery.loading) {
      return (
        <div className='loading'>
          <div>
            Loading...
          </div>
        </div>
      )
    }


    return (
      <div className='pokemons'>
          {this.props.allPokemonsQuery.allPokemons && this.props.allPokemonsQuery.allPokemons.map(poke => (
            <Poke key={poke.pokeId} name={poke.name} types={poke.types}/>
          ))}
      </div>
    )
  }
}

const ALL_POKEMONS_QUERY = gql`
  query allPokemons {
    allPokemons {
      name
      pokeId
      types {
        name
      }
    }
  }
`

const ListPokemonWithQuery = graphql(ALL_POKEMONS_QUERY, {
  name: 'allPokemonsQuery',
  options: {
    fetchPolicy: 'network-only',
    credentials: 'same-origin',
  },
})(ListPoke)

export default ListPokemonWithQuery
