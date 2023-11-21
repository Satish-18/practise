import React, { useState, useEffect } from 'react'
import data from './data'
import Article from './Article'

function App() {

  const [theme,setTheme] = useState('light-theme');

  const toogleTheme = () => {
    if (theme === 'light-theme') {
      setTheme('dark-theme')
    } else {
      setTheme('light-theme')
    }
  }

  useEffect(() => {
  document.documentElement.className = theme
  },[theme])
  return (
    <main>
      <nav className='nav-center'>
        <h1>overracted</h1>
        <button className="btn" onClick={toogleTheme}> 
        toogle</button>
      </nav>
      <section className='article'>
        {data.map((item) => {
          return(<Article id={item.id} {...item}/>)
        })}
      </section>
    </main>
  )
}

export default App
