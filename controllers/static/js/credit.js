const form = document.querySelector('.form')
form.addEventListener('submit', () => {
    let creditCardValue = document.querySelector('.credit').value
    cardnumber(creditCardValue)
})
function cardnumber(inputtxt)
console.log(inputtxt)
{
    var cardno = /^(?:5[1-5][0-9]{14})$/;
    var cardno2 = /^(?:4[0-9]{12}(?:[0-9]{3})?)$/;
    if(inputtxt.value.match(cardno2)) {
        return true;
        }
    else if(inputtxt.value.match(cardno)) {
        return true 
    }
    else
    {
    alert("Not a valid Visa credit card number!");
    return false;
    }
}
