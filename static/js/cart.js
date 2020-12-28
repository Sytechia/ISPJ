// Sending an Ajax call 
$('.cartBtn').click(function (event) {
    const id = event.target.parentElement.parentElement.children[0].children[1].innerText
    $.ajax({
        type: "GET",
        url: `/shop?id=${id}`
    })
})

//Focus and shows the 'add-to-cart' button
$(".txtb input").on("focus", function () {
    $(this).addClass("focus");
});

$(".txtb input").on("blur", function () {
    if ($(this).val() == "")
        $(this).removeClass("focus");
});

//Single product page magnifying glass 
$(".thumb-holder").append('<div class="thumb-zoom"></div>')
$(".thumb-holder").mousemove(function (event) {

    var offset = $(this).offset();
    var zoomX = event.pageX - offset.left - 50;
    var zoomY = event.pageY - offset.top - 50;


    $('.thumb-zoom').css({
        'left': zoomX,
        'top': zoomY,
    })

    var position = $(".thumb-zoom").position();
    var image = $(".thumbnail").attr('src');

    $('.thumb-zoom').html('<img id="zoom-img" src="' + image + '" >');

    $("#zoom-img").css({
        'left': -zoomX - 50,
        'top': -zoomY - 50,
    })

});

//cart logic

//Variables 
const addToCartBtnList = document.querySelectorAll('.cartBtn');
const searchField = document.querySelector('#searchBar')
const itemNames = document.querySelectorAll('.itemNames')
const cartTotal = document.querySelector('.Subtotal')
const cart = document.querySelector('.products')
const active = document.querySelector('.active1');
const singlebtn = document.querySelector('.singleProductBtn');

(()=> {
   
    if(active.innerHTML.includes('flask_login')){
        Array.from(addToCartBtnList).forEach(product => {
                product.disabled = true
        })
        document.querySelector('.checkout-button').href = '#'
    }

    check()
  
})();

function check(){
    if(document.querySelector('.item')){
        return ;
    }else{
         document.querySelector('.checkout-button').href = '#'
    }
}

//Event listeners 
if (searchField != null){
    searchField.addEventListener('keyup', searchBar);
};

// IIFE functions (Immediately Invoked Functions Upon Document Load)
(() => {
    let items = document.querySelectorAll('.item')
    Array.from(items).forEach(item => {
        let itemName = item.children[1].children[0].innerText
        Array.from(addToCartBtnList).forEach(product => {
            const productName = product.parentElement.parentElement.parentElement.children[1].children[0].children[0].innerText;
            if(itemName == productName){
                console.log(productName)
                product.disabled = true
            }
        })
    })
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
        check()
        const names = event.target.parentElement.parentElement.parentElement.children[1].children[0].innerText
        Array.from(addToCartBtnList).forEach(product => {
            const productName = product.parentElement.parentElement.parentElement.children[1].children[0].children[0].innerText;
            if(names == productName){
                product.disabled = false
            }
        })
        $.ajax({
            type: "GET",
            url: `/shop?delete=true&name=${names}`,
        })
    })
})();


(() => {
    Array.from(addToCartBtnList).forEach(btn => {
        btn.addEventListener('click', e => {
            const itemName = e.target.parentElement.parentElement.parentElement.children[1].children[0].children[0].innerText;
            const itemPrice = e.target.parentElement.parentElement.parentElement.children[1].children[1].children[0].innerText;
            let imgSrc = e.target.parentElement.parentElement.children[0].children[0].src;
            let position = imgSrc.indexOf("static");
            let partPath = imgSrc.slice(position);
            let item = {}
            item.name = itemName
            item.price = itemPrice
            item.quantity = 1
            item.src = partPath
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
            <div class="total-price">${item.price}</div>
            <div class="remove-product">
                <a href="#"><i class="fas fa-times"></i></a>
            </div>`
            divTemplate.innerHTML = template
            cart.insertBefore(divTemplate, cartTotal)
            total()

            document.querySelector('.checkout-button').href = '/checkout'
    
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
                check()
                const names = event.target.parentElement.parentElement.parentElement.children[1].children[0].innerText
                Array.from(addToCartBtnList).forEach(product => {
                    const productName = product.parentElement.parentElement.parentElement.children[1].children[0].children[0].innerText;
                    if(names == productName){
                        product.disabled = false
                    }
                })
                $.ajax({
                    type: "GET",
                    url: `/shop?delete=true&name=${names}`,
                })
            })

            btn.disabled = true
            swal({
                title: `${itemName} Added!`,
                text: "Item added successfully!",
                icon: "success",
                button: "Continue Shopping",
            })
        })
    })  
})();


//Search Bar Function 
function searchBar(e){
    const text = e.target.value 
    console.log(itemNames)
    Array.from(itemNames).forEach(item => {
        let names = item.innerText
        if(names.toLowerCase().indexOf(text) != -1){
        item.parentElement.parentElement.parentElement.style.display = 'block'
        console.log(item.parentElement.parentElement.parentElement)
        }else {
            item.parentElement.parentElement.parentElement.style.display = 'none'
        }
    })
}

//Update Cart Total upon quantity update and added item to cart 
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

//Remove Cart Item functionality 
function removeItem(e){ 
    let item = e.target.parentElement.parentElement.parentElement
    console.log(item)
    let itemprice = item.children[3].innerText
    var sliced2 = itemprice.substring(1)
    var slicedPrice2 = parseInt(sliced2)
    let quantityValue = parseInt(item.children[2].children[0].value)
    let amt = (quantityValue*slicedPrice2)
    item.remove()
    var total = document.querySelector('.totalPrice').textContent
    let sliced = total.substring(1)
    var slicedtotal = parseInt(sliced)
    document.querySelector('.totalPrice').textContent = `$${slicedtotal -= amt}`
    document.querySelector('.totalQuantity').textContent -= quantityValue
    check()
}