import React, {useState} from "react";

import gql from "graphql-tag";

import Poke from './UI/Poke'

import {useSubscription, useQuery} from "@apollo/client"

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
    const {data, loading} = useSubscription(
        SUBSCRIPTION_POKEMON_TRACKED,
        {variables: {pokeTypes: props.pokeTypes,}}
    );

    if (!data || loading) return <p></p>;

    const {event, pokemon} = data.pokeEvent
    return (
        <div className="container-fluid">
            <span>{event}</span>
            <div className="row">
                <Poke image={pokemon.imgDefaultField} name={pokemon.name} types={pokemon.types.edges}/>
            </div>
        </div>
    )
}

const TrackPoke = (props) => {
    const [typeOptions, setTypeOptions] = useState([]);
    const {data, loading, error} = useQuery(GET_ALL_TYPES, {});


    const handleOptions = (optionSelected) => {
        if (typeOptions.includes(optionSelected)) {
            setTypeOptions(typeOptions.filter((option) => option !== optionSelected))
        } else {
            setTypeOptions([...typeOptions, optionSelected])
        }
    };

    if (error) return <p>Error...</p>;
    if (loading) return <p>Loading...</p>;

    const dataAllTypes = data.allTypes.edges.map(edge => edge.node.name)

    return (
        <div>
            <h3>Add Type to Tracker</h3>

            {typeOptions.length ?
                <button onClick={() => setTypeOptions([])}>Reset</button> :
                <button onClick={() => setTypeOptions(dataAllTypes)}>All</button>
            }


            {dataAllTypes.map((option) => {
                return (
                    <button
                        key={`add` + option}
                        style={{backgroundColor: typeOptions.includes(option) ? 'green' : ''}}
                        onClick={() => handleOptions(option)}>
                        {option}
                    </button>
                )
            })}
            <div style={{minHeight: "200px", marginLeft: '10%'}}>
                <TrackeDisplay pokeTypes={typeOptions}/>
            </div>
        </div>
    )
};


export default TrackPoke