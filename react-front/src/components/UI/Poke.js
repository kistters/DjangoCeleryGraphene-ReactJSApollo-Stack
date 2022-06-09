import React from 'react';
import Type from './Type'

const poke = (props) => {

    
    return (
        <div className='col-sm-3'>
            <h4 className="text-primary">{props.name}</h4>
            <img src={props.image}  alt={props.name} />
            {props.types.map(type => (
                <Type key={props.name + type.node.name} name={type.node.name} />
            ))}
            <span>{props.children}</span>
        </div>
    )
}

export default poke;