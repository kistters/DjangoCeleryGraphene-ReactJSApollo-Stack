import React from 'react';

const poke = (props) => {
    return (
        <div className='poke'>
            <p>Name: {props.name}</p>
            <p>Types: {props.types}</p>
            <span>{props.children}</span>
        </div>
    )
}

export default poke;