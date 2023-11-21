import React, { useState } from 'react'
import SingleColor from './SingleColor'

import Values from  'values.js'

function App() {

  const [color, setColor] = useState('');
  const [error, setError] = useState(false);
  const [list, setList] = useState(new Values ('#f15052').all(10))


const  handleSubmit = (e) => {
  e.preventDefault();
  try {
      let colors = new Values (color).all(10)
      setList(colors)
      setError(false)
  } catch (error) {
    setError(true)
    console.log(error)
  }

}
  return (<>
    <section className='container'>
      <h3>Color Generator</h3>
      <form onSubmit={handleSubmit}>
          <input type="text" value={color} 
          placeholder='#e8e8e8' 
          className={`${error ? 'error' : null}`}
          onChange={(e) => setColor(e.target.value)}/>
       <button type='submit' className="btn" >submit</button>
      </form>
    </section>

    <section className='colors'>
      {list.map((color,index) => {
        console.log(color)
        return <SingleColor key={index} {...color} 
        index={index} hexColor={color.hex}/>
        
      })}
    </section>

    
</>  )
}

export default App