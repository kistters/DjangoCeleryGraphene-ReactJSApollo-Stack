import React from "react";

import gql from "graphql-tag";
import {useQuery} from "@apollo/client";

import Poke from './UI/Poke'

const ALL_POKEMONS_TYPE_QUERY = gql`
query allPokemons($type_name: String) {
    allPokemons(types_Name_Icontains: $type_name) {
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
`;

const ListPokeTypes = (props) => {
    const {loading, error, data} = useQuery(ALL_POKEMONS_TYPE_QUERY, {
        variables: { type_name: props.match.params.type_name}
    });
    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error :(</p>;
    var pokes = data.allPokemons

    return (
        <div className="container-fluid">
            <div className="row">
                {pokes.edges.map(poke => (
                    <div>
                        <Poke key={poke.node.pokeId} image={poke.node.imgDefaultField} name={poke.node.name}
                              types={poke.node.types.edges}/>
                    </div>
                ))}
            </div>
        </div>

    )
};

export default ListPokeTypes