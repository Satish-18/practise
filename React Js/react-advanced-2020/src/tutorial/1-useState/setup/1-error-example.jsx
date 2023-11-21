import React from 'react';



const ErrorExample = () => {
  let title = 'hello iam here'
  const hancleClick = () => {
  title = 'hello title'
  console.log('title')
};
return (
  <React.Fragment>
     <h2>{title}</h2>
      <button type='button' className='btn' onClick={hancleClick}>change title</button>
  </React.Fragment>
);
};

export default ErrorExample;
