// document.getElementsByClassName('cart-button').addEventListener(submit, (event) => {
//     event.preventDefault(
//     console.log(event.target.name)
    
//     )
// })

function getName(event){
    event.preventDefault()

    // console.log(event.target.name)
    itemName = event.target.name

    axios.get('/commerce/purchase', {params: {itemName: itemName}}).then((response) => {
        console.log('response?', response)
    })


}