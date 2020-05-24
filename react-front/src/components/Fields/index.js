import React, { useState } from "react";
import { useForm, ErrorMessage } from "react-hook-form";

export function Form({ defaultValues, children, onSubmit }) {
  const methods = useForm({ defaultValues });
  const { handleSubmit } = methods;

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      {Array.isArray(children)
        ? children.map(child => {
            return child.props.name
              ? React.createElement(child.type, {
                  ...{
                    ...child.props,
                    register: methods.register,
                    key: child.props.name
                  }
                })
              : child;
          })
        : children}
    </form>
  );
}

export function Input({ register, name, errors, ...rest }) {
  return (
      <>
        <input name={name} ref={register} {...rest} />
        <ErrorMessage errors={errors} name={name}  />
      </>
  )
}

export function Select({ register, options, name, errors, ...rest }) {
  return (
      <>
        <select name={name} ref={register} {...rest}>
        {options.map(option => (
            <option key={option.id} value={option.id}>{option.name}</option>
        ))}
        </select>
        <ErrorMessage errors={errors} name={name}  />
    </>
  )
}

export function MultipleSelect({ register, options, name, ...rest }) {
    const [choices, setChoices] = useState([])

    const onChangeHandle = ({target}) => {
        console.log(target.value)
        const options = [...target.options]
        const addChoice = !choices.includes(target.value)
        const newChoices = addChoice ? [...choices, target.value] : [...choices].filter(choice => choice !== target.value)
        
        options.map((option) => { option.selected = newChoices.includes(option.value) })
        
        setChoices(newChoices)
    }       

    return (
        <>
            <p>{choices}</p>
            <select name={name} multiple ref={register} {...rest} onChange={onChangeHandle}>
                {options.map(value => (
                <option key={value} value={value}>{value}</option>
                ))}
            </select>
        </>
    );
}

{/* <MultipleSelect name="choices" options={['instagram', 'blog']} register={register} /> */}