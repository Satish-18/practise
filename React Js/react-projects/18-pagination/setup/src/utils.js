const paginate = (followers) => {
    const itemsPerPage = 10;
    const page = Math.ceil(followers.length / itemsPerPage);
    console.log(page)

    const newFollowers = Array.from({length:page}, (_,index) => {
        const start = index * itemsPerPage
        return followers.slice(start,start + itemsPerPage)
    })
    return newFollowers
}

export default paginate
