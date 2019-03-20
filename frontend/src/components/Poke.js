import React from 'react';
import Type from '../components/Type'

const poke = (props) => {

    return (
        <div className='poke'>
            <p>Name: {props.name}</p>
            {props.types.map(type => (
                <Type key={props.name + type.name} name={type.name} />
            ))}
            <span>{props.children}</span>
        </div>
    )
}

export default poke;