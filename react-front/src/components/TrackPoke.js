import React, { useState } from "react";

import gql from "graphql-tag";

import Poke from '../components/Poke'

import { useSubscription, useQuery } from "@apollo/client"

const GET_ALL_TYPES = gql`
{
  allTypes {
    edges {
      node {
        name
      }
    }
  }
}`;

const SUBSCRIPTION_POKEMON_TRACKED = gql`
subscription trackPokeTypes($pokeTypes: [String]) {
  pokeEvent(trackPokeTypes: $pokeTypes) {
    event
    pokemon {
      pokeId
      name
      imgDefaultField
      imgDefault
      imgShiny
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
`;


const TrackeDisplay = (props) => {
  const { data, loading } = useSubscription(
    SUBSCRIPTION_POKEMON_TRACKED,
    { variables: { pokeTypes: props.pokeTypes, } }
  );

  if (!data) {
    return (
      <div className='loading'>
        <div>
          Loading...
        </div>
      </div>
    )
  }
  const { event, pokemon } = data.pokeEvent
  return (
    <div className="container-fluid">
      <span>{event}</span>
      <div className="row">
        <Poke image={pokemon.imgDefaultField} name={pokemon.name} types={pokemon.types.edges} />
      </div>
    </div>
  )
}

const TrackPoke = (props) => {
    const [pokeTypes, setType] = useState([]);
    const addType = (pokeType) => {
        if (!pokeTypes.includes(pokeType)) {
          setType([...pokeTypes, pokeType])
        }
    };

    const removeType = (pokeType) => {
      if (pokeTypes.includes(pokeType)) {
        setType(pokeTypes.filter(type => type !== pokeType))
      }
    };

    const { data, loading, error } = useQuery(GET_ALL_TYPES, {});
    
    if (error) {
      return (
        <div className='loading'>
          <div>
            Error...
          </div>
        </div>
      )
    } 

    if (loading) {
      return (
        <div className='loading'>
          <div>
            Loading...
          </div>
        </div>
      )
    } 

    const { edges: allTypes = [] } = data.allTypes
  
    return (
            <div>
              <h3>Add Type to Tracker</h3>
              {allTypes.map((edge) => edge.node).map((pokeType) => {
                const { name: TypeName } = pokeType
                return (
                  <button key={`add` + TypeName} onClick={() => addType(TypeName)}>
                  {TypeName}
                </button>
                )
              })}

              <div style={{minHeight: "200px", marginLeft: '10%'}}>
                <TrackeDisplay pokeTypes={pokeTypes} />
              </div>

              <p>Remove Type of Tracker</p>
              {pokeTypes.map((TypeName) => {
                return (
                <button key={`remove` + TypeName} onClick={() => removeType(TypeName)}>
                  {TypeName}
                </button>
                )
              })}
            </div>
    )
};


export default TrackPoke