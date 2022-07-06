// const findItem = async (event) => {
//     event.preventDefault()

//     let itemName = document.getElementById('search-value').value

//     // console.log(inquiry);

//     axios.post('/show-me-items', {itemName: itemName}).then((response)=>{
//         console.log('response? ', response)
//     });

// }

document.getElementById('search-form').addEventListener('submit', (event) => {
    
    event.preventDefault()

    const searchInput = document.getElementById('search-value')
    
    document.getElementById('search-result').innerHTML = ''

    axios.get('/commerce/products', {params: {query: searchInput.value}}).then((response) => {
        console.log('response?', response)
        let newImage = document.createElement('img')
        newImage.src = response.data.image_url
        document.getElementById('search-result').appendChild(newImage)
    })

    searchInput.value = ''

})
