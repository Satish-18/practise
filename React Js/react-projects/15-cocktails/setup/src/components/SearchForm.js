import React from 'react'
import { useGlobalContext } from '../context'

const SearchForm = () => {
  const {setSearchTerm} = useGlobalContext()
  const searchValue = React.useRef('');

  React.useEffect(() => {
    searchValue.current.focus()
  },[])
  
  const  searchCocktails = () => {
    setSearchTerm(searchValue.current.value)
  }

  const handleSubmit = (e) => {
    e.preventDefault()
  }

  return (
    <section className='section'>
      <form className='search-form' onSubmit={handleSubmit}>
        <div className='form-control'>
          <lable htmlFor='name'>search your favourate cocktail</lable>
          <input type='text' id='name' ref={searchValue}
          onChange={searchCocktails}/>       
        </div>
      </form>
    </section>
  )
}

export default SearchForm
