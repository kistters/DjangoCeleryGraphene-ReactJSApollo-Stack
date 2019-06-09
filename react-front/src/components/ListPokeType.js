import React from "react";

import gql from "graphql-tag";
import { Query } from "react-apollo";

import Poke from '../components/Poke'

const GET_DOGS = gql`
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

const ListPokeTypes = ({ classes, match }) => (
        <Query query={GET_DOGS} variables={{"type_name": match.params.type_name}}>
            {({ loading, error, data }) => {
                if (loading) return "Loading...";
                if (error) return `Error! ${error.message}`;
                var pokes = data.allPokemons
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

                );
            }}
        </Query>
);

export default ListPokeTypes