import React, { useEffect } from 'react'
import { useForm, ErrorMessage } from "react-hook-form"
import { Select, Input } from './Fields'
import { graphql } from 'react-apollo'
import gql from 'graphql-tag'


const Form = (props) => {    
    
    const { register, handleSubmit, errors, reset} = useForm({});

    const { 
        allTypes: { edges: pokeTypes } = {}, 
        allPokemons: { edges: pokemons } = {}, 
        loading 
    } = props.allPokemonTypesQuery
    

    useEffect(() => {
        // you can do async server request and fill up form
        if (loading) {
            return
        }

        setTimeout(() => {
          reset({
            username: 'luo_luo',
            email: 'luo@gmail.com',
            choices: ['blog', 'instagram'],
            pokeTypes: "VHlwZVR5cGU6OQ==",
            pokemons: ["UG9rZW1vblR5cGU6MTQ5", "UG9rZW1vblR5cGU6MTQ3"],
            social: {
                instagram: '@luo',
                prefers: ['blog', 'instagram']
            },
          });
        }, 2000);
    }, [reset, loading]);


    const onSubmit = data => {
        console.log(data);
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

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <div>
                <h5>Username:</h5>
                <Input 
                    name="username" 
                    errors={errors} 
                    register={register({ 
                        required: "This is required.", 
                        maxLength: { value: 30, message: "less then 30" } 
                    })} 
                />
            </div>
            
            <div>
                <h5>Email:</h5>
                <Input 
                    name="email"
                    errors={errors} 
                    register={register({
                        required: "This is required.",
                        pattern: {
                            value: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/, //eslint-disable-line
                            message: 'Not valid email'
                        },
                    })}
                />
            </div>

            <div>
                <h5>Instagram:</h5>
                <Input 
                    name="social.instagram" 
                    errors={errors} 
                    onChange={({ target }) => target.value = '@' + target.value.replace('@', '').toLowerCase() }
                    register={register({
                        required: "Social is required.", 
                        pattern: { 
                            value: /^@[a-z0-9_\.]+$/ , //eslint-disable-line
                            message: 'start with @ and only a-z and numerics'
                        }
                    })}
                />
            </div>
            <div>
                <h5>Pokemons</h5>
                <Select 
                    name="pokemons" 
                    multiple={true} 
                    errors={errors} 
                    options={pokemons.map(poke => { return poke.node } )} 
                    register={register({ 
                        required: "This is required.",
                        validate: {
                            lessThanThree: value => {
                                return Array.isArray(value) && value.length <= 3 || 'Less then 3!'
                            },
                          }
                    })} 
                />
            </div>
            
            <div>
                <h5>Poke Types</h5>
                <Select 
                    name="pokeTypes" 
                    errors={errors} 
                    options={pokeTypes.map(pokeType => { return pokeType.node } )} 
                    register={register({ 
                        required: "This is required.",
                        validate: {
                            checkType: value => {
                                const pokeType = pokeTypes
                                                    .filter(pokeType => pokeType.node.name ===  'fire')
                                                    .map(pokeType => { return pokeType.node })
                                const { id, name } = pokeType[pokeType.length - 1]
                                return value !== id  || 'Could not be ' + name + '!'
                            },
                          }
                        }
                    )} 
                />
            </div>
            <br />
            <button type="submit">Submit</button>
      </form>
    )
}


const ALL_POKEMON_TYPES_QUERY = gql`
{
    allTypes {
      edges {
        node {
          id
          name
        }
      }
    }
    allPokemons {
      edges {
        node {
          name
          id
          pokeId
        }
      }
    }
  }
  
`

const CustomForm = graphql(ALL_POKEMON_TYPES_QUERY, {
    name: 'allPokemonTypesQuery',
  })(Form)
  

export default CustomForm;