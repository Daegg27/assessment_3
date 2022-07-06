// const findItem = async (event) => {
//     event.preventDefault()

//     let itemName = document.getElementById('search-value').value

//     // console.log(inquiry);

//     axios.post('/show-me-items', {itemName: itemName}).then((response)=>{
//         console.log('response? ', response)
//     });

// }

document.getElementById('search-value').addEventListener('submit', (event) => {
    
    event.preventDefault()

    const inquiry = document.getElementById('search-value').value

    console.log(inquiry)


})