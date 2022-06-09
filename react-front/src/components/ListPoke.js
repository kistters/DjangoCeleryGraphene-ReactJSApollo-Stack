import React from 'react'
import { useQuery } from "@apollo/client";

import gql from 'graphql-tag'
import Poke from './UI/Poke'

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

const ListPoke = (props) => {
    const {loading, error, data} = useQuery(ALL_POKEMONS_QUERY);
    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error :(</p>;

    return (
        <div className="container-fluid">
            <div className="row">
                {data.allPokemons.edges.map((poke) => (
                    <Poke
                        key={poke.node.pokeId}
                        image={poke.node.imgDefaultField}
                        name={poke.node.name}
                        types={poke.node.types.edges}/>

                ))}
            </div>
        </div>
    );

};

export default ListPoke
