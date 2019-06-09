import React from 'react'
//import { Link } from 'react-router-dom'
import { graphql } from 'react-apollo'
import gql from 'graphql-tag'
import Poke from '../components/Poke'

class ListPoke extends React.Component {

  render(props) {

    if (this.props.allPokemonsQuery.loading) {
      return (
        <div className='loading'>
          <div>
            Loading...
          </div>
        </div>
      )
    }

    var pokes = this.props.allPokemonsQuery.allPokemons

    return (
      <div className="container-fluid">
        <div className="row">
          {pokes.edges.map(poke => (
            <div>
              <Poke key={poke.node.pokeId} image={poke.node.imgDefaultField} name={poke.node.name} types={poke.node.types.edges} />
            </div>
          ))}
        </div>
      </div>
    )
  }
}

const ALL_POKEMONS_QUERY = gql`
  query allPokemons {
    allPokemons {
      edges {
        node {
          name
          pokeId
          imgDefaultField
          types {
            edges {
              node {
                name
              }
            }
          }
        }
      }
    }
  }
`

const ListPokemonWithQuery = graphql(ALL_POKEMONS_QUERY, {
  name: 'allPokemonsQuery',
})(ListPoke)

export default ListPokemonWithQuery
