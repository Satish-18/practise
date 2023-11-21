import React, { useState } from 'react';

const UseStateObject = () => {
  const handleChange = () => {
   /*  setPerson({...person, message:'hello satish'}) */
   setMessage('hello this is the change')
  }
  const [person, setPerson ] = useState({name:'satish', age: 21, message:'hello world'});
  
  const [name, setName ] = useState('satish')
  const [age, setAge ] =useState(21)
  const [message, setMessage ] = useState('this is random message')
  return (
  <React.Fragment>
    <h3>{name}</h3>
    <h3>{age}</h3>
    <h3>{message}</h3>
    <button className="btn" onClick={handleChange}>change </button>
  </React.Fragment>
  )
};

export default UseStateObject;
