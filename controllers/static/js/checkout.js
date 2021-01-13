console.log('yes')

//Variables 
const items = document.querySelectorAll('.items');
const btn = document.querySelector('.confirm');
const cvv = document.querySelector('#cc-cvv')
const zip = document.querySelector('#zip')
const expiryyear = document.querySelector('#cc-expiration-year')
const expirymonth = document.querySelector('#cc-expiration-month')
const cardno = document.querySelector('#cc-number')


$(document).ready(function () {
    $('.confirm').submit(function(e) {
        if ($(this).data('submitted') === true) {
            // Form is already submitted
            console.log('Form is already submitted, waiting response.');
            // Stop form from submitting again
            e.preventDefault();
        } else {
            // Set the data-submitted attribute to true for record
            $(this).data('submitted', true);
        }
    });
});

//Event listeners 
cvv.addEventListener('keyup', e => {
    if(cvv.value.length > 3){
        cvv.value = cvv.value.slice(0, 3)
    }
})

zip.addEventListener('keyup', e => {
    if(zip.value.length > 6){
        zip.value = zip.value.slice(0, 6)
    }
})

expiryyear.addEventListener('keyup', e => {
    if(expiryyear.value.length > 4){
        expiryyear.value = expiryyear.value.slice(0, 4)
    }
})

expirymonth.addEventListener('keyup', e => {
    if(expirymonth.value.length > 2){
        expirymonth.value = expirymonth.value.slice(0, 2)
    }
})

cardno.addEventListener('keyup', e=> {
    if(cardno.value.length > 16){
        cardno.value = cardno.value.slice(0, 16)
    }
})

//Functions 
function validateEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

function validateName(name){
    let re =  /^[a-zA-Z\s]*$/;  
    return re.test(name)
}

function validateAddress(address){
    let re = /^[a-z0-9\s,'-]*$/i
    return re.test(address)
}

function validateNumbers(value){
    let re = /^\d+$/
    return re.test(value)
}

//event listeners 
btn.addEventListener('submit', e => {
    e.preventDefault()
    // e.preventDefault()
    const email = document.querySelector('#email')
    if(validateEmail(email.value) == false){
        e.preventDefault()
        swal.fire("Invalid Email", "Your email is invalid!", "error");
        return false
    }
    if(cvv.value.length < 3){
        e.preventDefault()
        swal.fire("Invalid CVV", "Your cvv needs to have 3 characters only", "error");
        return false
    }
    const name = document.querySelector('#firstName')
    if(validateName(name.value) == false){
        e.preventDefault()
        swal.fire("Invalid Name", "Your name field is invalid!", "error");
        return false
    }
    const cardname = document.querySelector('#cc-name')
    if(validateName(cardname.value) == false){
        e.preventDefault()
        swal.fire("Invalid Card Name", "Your card name field is invalid!", "error");
        return false
    }
    var d = new Date()
    var n = d.getMonth() + 1
    const expiryMonth = document.querySelector('#cc-expiration-month').value
    if(validateNumbers(expiryMonth) == false){
        e.preventDefault()
        swal.fire("Invalid card expiry month", "Your card expiry month field is invalid!", "error");
        return false
    }
    if(expiryMonth < n){
        e.preventDefault()
        swal.fire("Invalid card expiry month", "Your card expiry month field is invalid!", "error");
        return false
    } else if(expiryMonth > 12){
        e.preventDefault()
        swal.fire("Invalid card expiry month", "Your card expiry month field is invalid!", "error");
        return false
    }
    const expiryYear = document.querySelector('#cc-expiration-year').value
    if(expiryYear.length < 4){
        e.preventDefault()
        swal.fire("Invalid card expiry year", "Your card expiry year field is invalid!", "error");
        return false
    }
    if(validateNumbers(expiryYear) == false){
        e.preventDefault()
        swal.fire("Invalid card expiry year", "Your card expiry year field is invalid!", "error");
        return false
    }
    if(expiryYear < 2020){
        e.preventDefault()
        swal.fire("Invalid card expiry year", "Your card expiry year field is invalid!", "error");
        return false
    } else if(expiryYear > 2028){
        e.preventDefault()
        swal.fire("Invalid card expiry year", "Your card expiry year field is invalid!", "error");
        return false
    }
    const state = document.querySelector('#state')
    if(validateName(state.value) == false){
        e.preventDefault()
        swal.fire("Invalid State", "Your state field is invalid!", "error");
        return false
    }
    if(zip.value.length < 6){
        e.preventDefault()
        swal.fire("Invalid Zip", "Your zip needs to have 6 characters only", "error");
        return false
    }
    const address = document.querySelector('#address')
    if(validateAddress(address.value) == false){
        e.preventDefault()
        swal.fire("Invalid Address", "Your address field is invalid!", "error");
        return false
    }
    if(validateNumbers(cvv.value) == false){
        e.preventDefault()
        swal.fire("Invalid CVV", "Your cvv field is invalid", "error");
        return false
    }
    $.ajax({
        type:"GET",
        async:false,
        url:`/validateCardNo?cardno=${cardno.value}`,
        success:function(data){
            if(data == "False"){
                console.log(data)
                e.preventDefault()
                swal.fire("Invalid Card Number", "Your card number is invalid", "error");
                return false
            }
        }
    })
    document.querySelector('.checkout').disabled = true;
    console.log('fired')
    // $.ajax({
    //     type: "GET",
    //     url: `/otp`,
    //     success: function(){
    //         window.location.href = '/userOTP'
    //     }
    // })
    $.ajax({
        type:"POST",
        url:"/paymentConfirmation"
    })
    window.location.href = '/myAccount'
});



//IIFE (Immediately invoked Functions upon document load)
(()=> {
let totalPrice = 0
let totalQuantity = 0
Array.from(items).forEach(item => {
    let itemPrice = parseFloat(item.children[1].children[0].innerText);
    let itemQuantity = parseInt(item.children[0].children[1].children[0].innerText);
    totalPrice += (itemPrice * itemQuantity)
    totalQuantity += itemQuantity
})
document.querySelector('.badge-pill').textContent = totalQuantity
document.querySelector('.total').textContent = "$" + totalPrice
})();