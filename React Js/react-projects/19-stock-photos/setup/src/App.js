import React, { useState, useEffect } from 'react'
import { FaSearch } from 'react-icons/fa'
import Photo from './Photo'
// const clientID = `?client_id=${process.env.REACT_APP_ACCESS_KEY}`
const mainUrl = `https://api.unsplash.com/photos/`
const searchUrl = `https://api.unsplash.com/search/photos/`

function App() {
  const [loading, setLoading] = useState(false)
  const [photos, setPhotos] = useState([])

  const fetchImages = async () => {
    let url ;
    url = `${mainUrl}?client_id=i_ywvnK7cJzDbIJ3lJ6ht3DlwaPYX3qSSm8
    ZmihfsZ0`
    try {
      const response = await fetch(url)
      const data  = await response.json()
    console.log(data)
    } catch (error) {
     console.log(error) 
    }
  }

  useEffect(() => {
    fetchImages()
  },[])
  return <h2>stock photos starter</h2>
}

export default App
