//Variables
const btn = document.querySelectorAll('.singleProductBtn');

//Event listeners
Array.from(btn).forEach(prod  => {
    prod.addEventListener('click', addToCart)
});

//IIFE
(() => {
    let items = document.querySelectorAll('.item')
    Array.from(items).forEach(item => {
        let itemName = item.children[1].children[0].innerText
        Array.from(btn).forEach(product => {
            const productName = product.parentElement.parentElement.children[0].children[0].children[0].innerText
            console.log(productName)
            if(itemName == productName){
                product.disabled = true
            }
        })
    })
})();

//Functions

//Add to cart functionality 
function addToCart(e){
    const name = e.target.parentElement.parentElement.children[0].children[0].innerText
    let price = e.target.parentElement.parentElement.children[0].children[1].innerText
    let slicedprice = price.substring(1)
    let sliced = parseInt(slicedprice)
    let img = e.target.parentElement.parentElement.parentElement.children[0].children[0].children[0].src
    let position = img.indexOf("static");
    let partPath = img.slice(position);
    console.log(partPath)
    let item = {}
    item.name = name 
    item.quantity = 1
    item.src = partPath
    item.price = sliced
    let divTemplate = document.createElement('div')
            divTemplate.classList.add('item')
            let template = `<div class="image">
            <img src="../${item.src}" alt="" height="80px">
            </div>
            <div class="description">
                <span>${item.name}</span>
            </div>
            <div class="quantity">
                <input type="text" name="name" class="quan" value="${item.quantity}">
            </div>
            <div class="total-price">$${item.price}</div>
            <div class="remove-product">
                <a href="#"><i class="fas fa-times"></i></a>
            </div>`
            divTemplate.innerHTML = template
            cart.insertBefore(divTemplate, cartTotal)
            total()
    
            let removeBtn = document.querySelectorAll('.fa-times')
            Array.from(removeBtn).forEach(btn => {
                btn.addEventListener('click', removeItem)
            })

            let productQuantityChange = document.querySelectorAll('.quan')
            Array.from(productQuantityChange).forEach(btn => {
                btn.addEventListener('change', total)
            })

            $('.quan').change(function (event) {
                const name = event.target.parentElement.parentElement.children[1].children[0].innerText
                const quantity = event.target.parentElement.parentElement.children[2].children[0].value
                $.ajax({
                    type: "GET",
                    url: `/shop?name=${name}&quantity=${quantity}`,
                })
            })

            $('.fa-times').click(function (event) {
                const names = event.target.parentElement.parentElement.parentElement.children[1].children[0].innerText
                Array.from(btn).forEach(product => {
                    const productName = product.parentElement.parentElement.children[0].children[0].children[0].innerText;
                    if(names == productName){
                        product.disabled = false
                    }
                })
                $.ajax({
                    type: "GET",
                    url: `/shop?delete=true&name=${names}`,
                })
            })
}

//Calculate total function 
function total(){
    let total = 0
    let quantity = 0
    let cartItems = document.querySelectorAll('.item')
    Array.from(cartItems).forEach(item => {
        let itemprice = item.children[3].innerText
        var sliced = itemprice.substring(1)
        var slicedPrice = parseInt(sliced)
        let quantityValue = parseInt(item.children[2].children[0].value)
        total += (quantityValue*slicedPrice)
        quantity += quantityValue
        document.querySelector('.totalPrice').textContent = `$${total}`
        document.querySelector('.totalQuantity').textContent = quantity
    })
}