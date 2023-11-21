import React, { useState, useEffect } from 'react'
import { FaAngleDoubleRight } from 'react-icons/fa'
// ATTENTION!!!!!!!!!!
// I SWITCHED TO PERMANENT DOMAIN
const url = 'https://course-api.com/react-tabs-project'

function App() {
const [loading, setLoading] = useState(true);
const [jobs, setJobs] = useState([]);
const [value, setValue] = useState(0)

  const fetchTabs =  async() => {
    const response = await fetch(url);
    const tabs =  await response.json();
    setJobs(tabs);
    setLoading(false);
    
    
  }

useEffect(() => {
  fetchTabs();
},[])

if(loading) {
  return (
    <section className='section loading'>
      <h1>Loading...</h1>
    </section>
  )
}

const {company, dates, duties, title} = jobs[value];
return (
  <section className='section'>
    <div className='title'>
      <h2>
        Expierence
      </h2>
       </div>
      <div className='underline'></div>
      <div className='jobs-center'>
       
        <div className='container'>
          {
            jobs.map((item,index)=> {
              return <button key={item.id} onClick={()=> setValue(index)} className={`job-btn ${index === value && 'active-btn'}`}>
                {item.company}
                </button>
            })
          }
        </div>
        
        <article className='job-info'>
          <h3>
            {title}
          </h3>
          <h4>
            {company}
          </h4>
          <p className='job-dates'>{dates}</p>
        {duties.map((duty,index) => {
          return <div key={index} className='job-desc'>
            <FaAngleDoubleRight className='job-icon'></FaAngleDoubleRight>
          <p>{duty}</p>
          </div>
        })}
        </article>
    </div>
  </section>
);
}

export default App
