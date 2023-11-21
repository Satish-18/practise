import React, { useState } from 'react';
import { AiOutlineMinus, AiOutlinePlus } from 'react-icons/ai';
const Question = ({title,info}) => {
  const [ismore, setIsMore ] = useState(false);

  return( 
  <article className='question'>
    <header>
      <h4>{title}</h4>
       <button className='btn' onClick={() => setIsMore(!ismore)}>{ismore ? <AiOutlineMinus/> : <AiOutlinePlus/>}</button>
        
    </header>
    <p>{ismore ? info : ''}</p>
  </article>
  );
 
};

export default Question;
