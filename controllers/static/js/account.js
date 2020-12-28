//Variables 
let editAddressBtn = document.querySelectorAll('.editAddress');
let removeAddressBtn = document.querySelectorAll('.removeAddress');
let reviewBtn = document.querySelectorAll('.showReviewSection');
let submitReviewBtn = document.querySelectorAll('.submit-review');
let rating = document.querySelectorAll('.reviewDetails');
let editReview = document.querySelectorAll('.editReview');
let removeReview = document.querySelectorAll('.removeReview');
let submitEditReviewBtn = document.querySelectorAll('.edit-submit-review');
let removeCardBtn = document.querySelectorAll('.removeWallet');
let setDefaultAddressBtn = document.querySelectorAll('.setAsDefault');
let setDefaultCardBtn = document.querySelectorAll('.setAsDefaultWallet');
let transaction_dates = document.querySelectorAll('.tran_date');


//IIFE 
(() => {
    Array.from(removeAddressBtn).forEach(btn => {
        btn.addEventListener('click', removeAddress)
    })

    Array.from(removeCardBtn).forEach( btn => {
      btn.addEventListener('click', removeCard)
    })

    Array.from(reviewBtn).forEach(btn => {
      btn.addEventListener('click', identity)
    })

    Array.from(submitReviewBtn).forEach(btn => {
      btn.addEventListener('click', postReview)
    })

    Array.from(removeReview).forEach(review => {
      review.addEventListener('click', removeReviewfunc)
    })

    Array.from(editReview).forEach(review => {
      review.addEventListener('click', identity2)
    })

    Array.from(submitEditReviewBtn).forEach(review => {
      review.addEventListener('click', postReview2)
    })

    Array.from(setDefaultAddressBtn).forEach(btn => {
      btn.addEventListener('click', defaultAddress)
    })

    Array.from(setDefaultCardBtn).forEach(btn => {
      btn.addEventListener('click', defaultCard)
    })

    Array.from(transaction_dates).forEach(date => {
      console.log('u=y')
      let orginal = date.value 
      let amorpm = parseInt(orginal.slice(11,13))
      let adjusted = orginal.slice(0,-10)
      let day;
      if(amorpm > 12){
        day = 'pm'
      } else{
        day ='am'
      }
      date.value = adjusted + day
    })
})();

//Functions 

/*
  * Removing of address functionality
*/
function removeAddress(e){
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
          confirmButton: 'btn btn-success',
          cancelButton: 'btn btn-danger'
        },
        buttonsStyling: true
      })
      
      swalWithBootstrapButtons.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Yes, delete it!',
        cancelButtonText: 'No, cancel!',
        reverseButtons: true
      }).then((result) => {
        if (result.value) {
          swalWithBootstrapButtons.fire(
            'Deleted!',
            'Your address has been deleted.',
            'success'
          )
          e.target.parentElement.remove()
            const address = e.target.parentElement.children[0].innerText
            $.ajax({
                type: "GET",
                url: `/myAccount?delete=true&address=${address}`,
            })
        } else if (
          /* Read more about handling dismissals below */
          result.dismiss === Swal.DismissReason.cancel
        ) {
          swalWithBootstrapButtons.fire(
            'Cancelled',
            'Your address is safe :)',
            'error'
          )
        }
      })
}

/*
  * Removing of Credit card details
*/
function removeCard(e){
  const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
        confirmButton: 'btn btn-success',
        cancelButton: 'btn btn-danger'
      },
      buttonsStyling: true
    })
    
    swalWithBootstrapButtons.fire({
      title: 'Are you sure?',
      text: "You won't be able to revert this!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Yes, delete it!',
      cancelButtonText: 'No, cancel!',
      reverseButtons: true
    }).then((result) => {
      if (result.value) {
        swalWithBootstrapButtons.fire(
          'Deleted!',
          'Your card has been deleted.',
          'success'
        )
        const card = e.target.parentElement.children[0].innerText
        $.ajax({
          type: "GET",
          url: `/myAccount?delete=true&card=${card}`,
      })
          console.log(card)
        e.target.parentElement.parentElement.parentElement.parentElement.remove()
          
          
      } else if (
        /* Read more about handling dismissals below */
        result.dismiss === Swal.DismissReason.cancel
      ) {
        swalWithBootstrapButtons.fire(
          'Cancelled',
          'Your card is safe :)',
          'error'
        )
      }
    })
}

/*
  * Assigns item name to the review modal in order to be accessed by ajax
*/
function identity(event){
  const itemName = event.target.parentElement.children[0].innerText
  document.querySelector('.modal-title').innerHTML = `Write a Review for <span>${itemName}</span>`
}

/*
  * Ajax + posting of address functionality
*/
function postReview(event) {
  let rating; 
  let parent = event.target.parentElement.parentElement
  let itemName = parent.children[0].children[0].children[0].textContent
  let id = parent.children[0].children[1].textContent
  let reviewInputs = document.querySelectorAll('input[type="radio"]')
  Array.from(reviewInputs).forEach(radio => {
    if(radio.checked){
      rating = radio.value
    }
  })
  let reviewMessage = parent.children[2].children[0].value
  if(rating){
    $.ajax({
      type: "GET",
      url: `/review?name=${itemName}&rating=${rating}&message=${reviewMessage}&id=${id}`,
  })
  $.ajax({
    type: "GET",
    url: `/myAccount`,
})
  } 
}

/*
  * Removing of review posted by user
*/
function removeReviewfunc(e){
  const swalWithBootstrapButtons = Swal.mixin({
    customClass: {
      confirmButton: 'btn btn-success',
      cancelButton: 'btn btn-danger'
    },
    buttonsStyling: true
  })
  
  swalWithBootstrapButtons.fire({
    title: 'Are you sure?',
    text: "You won't be able to revert this!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonText: 'Yes, delete it!',
    cancelButtonText: 'No, cancel!',
    reverseButtons: true
  }).then((result) => {
    if (result.value) {
      swalWithBootstrapButtons.fire(
        'Deleted!',
        'Your review  has been deleted.',
        'success'
      )
      const itemName = e.target.parentElement.parentElement.children[1].children[0].children[0].innerText
      console.log(itemName)
      e.target.parentElement.parentElement.parentElement.remove()
        $.ajax({
            type: "GET",
            url: `/myAccount?delete=true&name=${itemName}`,
        })
    } else if (
      /* Read more about handling dismissals below */
      result.dismiss === Swal.DismissReason.cancel
    ) {
      swalWithBootstrapButtons.fire(
        'Cancelled',
        'Your address is safe :)',
        'error'
      )
    }
  })
}

/*
  * Assigns the item name to the review edit modal 
*/
function identity2(event){ 
  const itemName = event.target.parentElement.parentElement.children[1].children[0].children[0].textContent
  document.querySelector('#modal-title').innerHTML = `Write a Review for <span>${itemName}</span>`
}

/*
  * Ajax + posting of editted review 
*/
function postReview2(event) {
  let rating; 
  let parent = event.target.parentElement.parentElement
  let itemName = parent.children[0].children[0].children[0].textContent
  let id = parent.children[0].children[1].textContent
  let reviewInputs = document.querySelectorAll('input[type="radio"]')
  Array.from(reviewInputs).forEach(radio => {
    if(radio.checked){
      rating = radio.value
    }
  })
  console.log(rating)
  let reviewMessage = parent.children[2].children[0].value
  if(rating){
    $.ajax({
      type: "GET",
      url: `/review?edit=true&name=${itemName}&rating=${rating}&message=${reviewMessage}&id=${id}`,
  })
  } 
}

/*
  * Ajax + Setting of Default address
*/
function defaultAddress(event) {
  Array.from(setDefaultAddressBtn).forEach(btn => {
    btn.innerHTML = 'Set as Default address'
  })
  event.target.innerHTML = 'Default Address'
  let x = event.target.parentElement
  let old = document.querySelectorAll('.default-add')
  Array.from(old).forEach(x => {
    x.classList.remove('default-add')
  })
  x.classList.add('default-add')
  const address = event.target.parentElement.children[0].innerText
  $.ajax({
    type:'GET',
    url:`/defaultAddress?address=${address}`,
  })
}

/*
  * Ajax + setting of Default Card
*/
function defaultCard(event) {
  Array.from(setDefaultCardBtn).forEach(btn => {
    btn.innerHTML = 'Set as Default card'
  })
  event.target.innerHTML = 'Default card'
  let x = event.target.parentElement.parentElement.parentElement.parentElement
  let old = document.getElementsByClassName('default')
  Array.from(old).forEach(x => {
    x.classList.remove('default')
  })
  x.classList.add('default')
  const card = event.target.parentElement.children[0].innerText
  $.ajax({
    type:'GET',
    url:`/defaultCard?card=${card}`
  })
}

// var disable = document.querySelector(".disable")
// disable.addEventListener('click', function(){
//   window.location.href="/disable"
// })
var disable = document.querySelector(".disable")
if(disable){
disable.addEventListener('click', function(){
  window.location.href="/disable"
})
}



$('.fixed').on('keyup', validatetext);

function validatetext(e) {
    var w = parseInt(e.target.value.length);
    if (w > 16) {
        console.log("Width Gt 100px ["+w+"px] Char Count ["+e.target.value.length+"]");
        do {
            e.target.value = e.target.value.slice(0,-1);
        } while (parseInt(e.target.value.length) > 16)
    } else {
        console.log("Keep going! ["+w+"px] Char Count ["+e.target.value.length+"]");
    }
}
/*cancle button edit address */
// let cancel_btn = document.querySelector('.cancel_add')
// cancel_btn.addEventListener('click', e=> {
//   console.log('yes')
//   window.location.href = '/myAccount'
// })
if (document.querySelector('#current_password') != null){
document.querySelector('#current_password').addEventListener('keyup', event=> {
  let old_password = event.target.value
  $.ajax({
    type: "GET",
    url: `/myAccount?old=${old_password}`,
    success: function(data){
      if(data == "wrong"){
        event.target.classList.add('is-invalid')
        document.querySelector('#password').disabled = true
        document.querySelector('#confirm_password').disabled = true
        if(document.querySelector('#wrong')){
          return false
        } else{
        $('#current_password').after(`<span id="wrong" class="text-danger">Wrong password!</span></br>`)
        }
    } else {
      document.querySelector('#wrong').classList.remove("text-danger")
      document.querySelector("#wrong").classList.add("text-success")
      document.querySelector('#wrong').innerText = "Correct password!"
      event.target.classList.remove('is-invalid')
      document.querySelector('#password').disabled = false
      document.querySelector('#confirm_password').disabled = false
      let new_password = document.querySelector('#password')
        let confirm_password = document.querySelector('#confirm_password').value
        var meter = document.getElementById('password-strength-meter');
        var text = document.getElementById('password-strength-text');
        let regsiterbtn = document.getElementById('changepassword');
        new_password.addEventListener('keyup', function() {
          meter.style.display = 'block'
          text.style.display = 'block'
          meter.value = ''
          var val = new_password.value;
          // const common = Array("123456","password","12345678","123456789","1234","pussy","12345","dragon","qwerty","696969","mustang","letmein","baseball","master","michael","football","shadow","monkey","abc123","pass","6969","jordan","harley","ranger","iwantu","jennifer","hunter","2000","test","batman","trustno1","thomas","tigger","robert","access","love","buster","1234567","soccer","hockey","killer","george","sexy","andrew","charlie","superman","asshole","dallas","jessica","panties","pepper","1111","austin","william","daniel","golfer","summer","heather","hammer","yankees","joshua","maggie","biteme","enter","ashley","thunder","cowboy","silver","richard","orange","merlin","michelle","corvette","bigdog","cheese","matthew","121212","patrick","martin","freedom","ginger","blowjob","nicole","sparky","yellow","camaro","secret","dick","falcon","taylor","111111","131313","123123","bitch","hello","scooter","please","","porsche","guitar","chelsea","black","diamond","nascar","jackson","cameron","654321","computer","amanda","wizard","xxxxxxxx","money","phoenix","mickey","bailey","knight","iceman","tigers","purple","andrea","horny","dakota","aaaaaa","player","sunshine","morgan","starwars","boomer","cowboys","edward","charles","girls","booboo","coffee","xxxxxx","bulldog","ncc1701","rabbit","peanut","john","johnny","gandalf","spanky","winter","brandy","compaq","carlos","tennis","james","mike","brandon","fender","anthony","blowme","ferrari","cookie","chicken","maverick","chicago","joseph","diablo","sexsex","hardcore","666666","willie","welcome","chris","panther","yamaha","justin","banana","driver","marine","angels","fishing","david","maddog","hooters","wilson","butthead","dennis","captain","bigdick","chester","smokey","xavier","steven","viking","snoopy","blue","eagles","winner","samantha","house","miller","flower","jack","firebird","butter","united","turtle","steelers","tiffany","zxcvbn","tomcat","golf","bond007","bear","tiger","doctor","gateway","gators","angel","junior","thx1138","porno","badboy","debbie","spider","melissa","booger","1212","flyers","fish","porn","matrix","teens","scooby","jason","walter","cumshot","boston","braves","yankee","lover","barney","victor","tucker","princess","mercedes","5150","doggie","zzzzzz","gunner","horney","bubba","2112","fred","johnson","xxxxx","tits","member","boobs","donald","bigdaddy","bronco","penis","voyager","rangers","birdie","trouble","white","topgun","bigtits","bitches","green","super","qazwsx","magic","lakers","rachel","slayer","scott","2222","asdf","video","london","7777","marlboro","srinivas","internet","action","carter","jasper","monster","teresa","jeremy","11111111","bill","crystal","peter","pussies","cock","beer","rocket","theman","oliver","prince","beach","amateur","7777777","muffin","redsox","star","testing","shannon","murphy","frank","hannah","dave","eagle1","11111","mother","nathan","raiders","steve","forever","angela","viper","ou812","jake","lovers","suckit","gregory","buddy","whatever","young","nicholas","lucky","helpme","jackie","monica","midnight","college","baby","brian","mark","startrek","sierra","leather","232323","4444","beavis","bigcock","happy","sophie","ladies","naughty","giants","booty","blonde","golden","0","fire","sandra","pookie","packers","einstein","dolphins","0","chevy","winston","warrior","sammy","slut","8675309","zxcvbnm","nipples","power","victoria","asdfgh","vagina","toyota","travis","hotdog","paris","rock","xxxx","extreme","redskins","erotic","dirty","ford","freddy","arsenal","access14","wolf","nipple","iloveyou","alex","florida","eric","legend","movie","success","rosebud","jaguar","great","cool","cooper","1313","scorpio","mountain","madison","987654","brazil","lauren","japan","naked","squirt","stars","apple","alexis","aaaa","bonnie","peaches","jasmine","kevin","matt","qwertyui","danielle","beaver","4321","4128","runner","swimming","dolphin","gordon","casper","stupid","shit","saturn","gemini","apples","august","3333","canada","blazer","cumming","hunting","kitty","rainbow","112233","arthur","cream","calvin","shaved","surfer","samson","kelly","paul","mine","king","racing","5555","eagle","hentai","newyork","little","redwings","smith","sticky","cocacola","animal","broncos","private","skippy","marvin","blondes","enjoy","girl","apollo","parker","qwert","time","sydney","women","voodoo","magnum","juice","abgrtyu","777777","dreams","maxwell","music","rush2112","russia","scorpion","rebecca","tester","mistress","phantom","billy","6666","albert");
          // Update the password strength meter
          console.log(val)
          let meter_value; 
          $.ajax({
            type: "GET",
            url: `/checkPassword?pass=${escape(val)}`, 
            success:function(data){
              let parsed= JSON.parse(data)
              console.log(val)
              console.log(parsed)
              if (parseFloat(parsed['data'][0]) < 0.20 && parseFloat(parsed['data'][0]) >= 0){
                meter_value = 0
              } 
              else if (parseFloat(parsed['data'][0]) < 0.44 && parseFloat(parsed['data'][0]) >= 0.20){
                meter_value = 1
              }
              else if (parseFloat(parsed['data'][0]) < 0.61 && parseFloat(parsed['data'][0]) >= 0.44){
                meter_value = 2
              }
              else if (parseFloat(parsed['data'][0]) < 0.8 && parseFloat(parsed['data'][0]) >= 0.61){
                meter_value = 3
              } else{
                meter_value = 4
              }
              let requirements = eval(parsed['data'][1])
              console.log(requirements.length)
              if(requirements.length != 0){
                meter_value = 1;
                regsiterbtn.disabled = true
              }else if (meter_value < 2){
                  regsiterbtn.disabled = true
              }else{
                regsiterbtn.disabled = false
              }
              meter.value = meter_value
              if (val !== "") {
                text.innerHTML = "Strength: " + strength[meter_value]; 
                requirements.forEach(ele => {
                  if(ele == "Length(8)"){
                    text.innerHTML += "<br><span style=color:red>Minimum length of 8 required</span>"
                  }
                  if (ele == "Uppercase(2)"){
                    text.innerHTML += "<br><span style=color:red>Minimum of two uppercases characters requried</span>"
                  }
                  if (ele == "Numbers(2)"){
                    text.innerHTML += "<br><span style=color:red>Minimum of two numbers requried</span>"
                  }
                  if (ele == "Special(2)"){
                    text.innerHTML += "<br><span style=color:red>Minimum of two special characters requried</span>"
                  }
                  if (ele == "Nonletters(2)"){
                    text.innerHTML += "<br><span style=color:red>Minimum of two non-letters characters requried</span>"
                  }
                })
              } else {
                text.innerHTML = "";
              }
            }
          })
          // Update the text indicator
        });
      $('#changepassword').click(()=> {
        let confirm_password = document.querySelector('#confirm_password').value
        let new_password = document.querySelector('#password').value
        console.log('fired')
        if(confirm_password != new_password){
          Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'New password is not the same!'
          })
          return false 
        } 
        else {
          $.ajax({
            type: "GET",
            url: `/myAccount?new=${new_password}`, 
            success:function(data){
              window.location.href=`http://127.0.0.1:5000/myAccount`
            }
          })
        }
      })
    }
  }
})
})
}

var strength = {
  0: "Worst",     //0 - 0.19
  1: "Bad",      //0.2 - 0.43
  2: "average", //0.44 - 0.6
  3: "Good",   //0.61 - 0.8
  4: "Strong" //0.81 - 1
};
var password = document.getElementById('password');
var meter = document.getElementById('password-strength-meter');
var text = document.getElementById('password-strength-text');
var regsiterbtn = document.getElementById('submit');


password.addEventListener('keyup', function() {
  meter.style.display = 'block'
  text.style.display = 'block'
  meter.value = ''
  var val = password.value;
  // const common = Array("123456","password","12345678","123456789","1234","pussy","12345","dragon","qwerty","696969","mustang","letmein","baseball","master","michael","football","shadow","monkey","abc123","pass","6969","jordan","harley","ranger","iwantu","jennifer","hunter","2000","test","batman","trustno1","thomas","tigger","robert","access","love","buster","1234567","soccer","hockey","killer","george","sexy","andrew","charlie","superman","asshole","dallas","jessica","panties","pepper","1111","austin","william","daniel","golfer","summer","heather","hammer","yankees","joshua","maggie","biteme","enter","ashley","thunder","cowboy","silver","richard","orange","merlin","michelle","corvette","bigdog","cheese","matthew","121212","patrick","martin","freedom","ginger","blowjob","nicole","sparky","yellow","camaro","secret","dick","falcon","taylor","111111","131313","123123","bitch","hello","scooter","please","","porsche","guitar","chelsea","black","diamond","nascar","jackson","cameron","654321","computer","amanda","wizard","xxxxxxxx","money","phoenix","mickey","bailey","knight","iceman","tigers","purple","andrea","horny","dakota","aaaaaa","player","sunshine","morgan","starwars","boomer","cowboys","edward","charles","girls","booboo","coffee","xxxxxx","bulldog","ncc1701","rabbit","peanut","john","johnny","gandalf","spanky","winter","brandy","compaq","carlos","tennis","james","mike","brandon","fender","anthony","blowme","ferrari","cookie","chicken","maverick","chicago","joseph","diablo","sexsex","hardcore","666666","willie","welcome","chris","panther","yamaha","justin","banana","driver","marine","angels","fishing","david","maddog","hooters","wilson","butthead","dennis","captain","bigdick","chester","smokey","xavier","steven","viking","snoopy","blue","eagles","winner","samantha","house","miller","flower","jack","firebird","butter","united","turtle","steelers","tiffany","zxcvbn","tomcat","golf","bond007","bear","tiger","doctor","gateway","gators","angel","junior","thx1138","porno","badboy","debbie","spider","melissa","booger","1212","flyers","fish","porn","matrix","teens","scooby","jason","walter","cumshot","boston","braves","yankee","lover","barney","victor","tucker","princess","mercedes","5150","doggie","zzzzzz","gunner","horney","bubba","2112","fred","johnson","xxxxx","tits","member","boobs","donald","bigdaddy","bronco","penis","voyager","rangers","birdie","trouble","white","topgun","bigtits","bitches","green","super","qazwsx","magic","lakers","rachel","slayer","scott","2222","asdf","video","london","7777","marlboro","srinivas","internet","action","carter","jasper","monster","teresa","jeremy","11111111","bill","crystal","peter","pussies","cock","beer","rocket","theman","oliver","prince","beach","amateur","7777777","muffin","redsox","star","testing","shannon","murphy","frank","hannah","dave","eagle1","11111","mother","nathan","raiders","steve","forever","angela","viper","ou812","jake","lovers","suckit","gregory","buddy","whatever","young","nicholas","lucky","helpme","jackie","monica","midnight","college","baby","brian","mark","startrek","sierra","leather","232323","4444","beavis","bigcock","happy","sophie","ladies","naughty","giants","booty","blonde","golden","0","fire","sandra","pookie","packers","einstein","dolphins","0","chevy","winston","warrior","sammy","slut","8675309","zxcvbnm","nipples","power","victoria","asdfgh","vagina","toyota","travis","hotdog","paris","rock","xxxx","extreme","redskins","erotic","dirty","ford","freddy","arsenal","access14","wolf","nipple","iloveyou","alex","florida","eric","legend","movie","success","rosebud","jaguar","great","cool","cooper","1313","scorpio","mountain","madison","987654","brazil","lauren","japan","naked","squirt","stars","apple","alexis","aaaa","bonnie","peaches","jasmine","kevin","matt","qwertyui","danielle","beaver","4321","4128","runner","swimming","dolphin","gordon","casper","stupid","shit","saturn","gemini","apples","august","3333","canada","blazer","cumming","hunting","kitty","rainbow","112233","arthur","cream","calvin","shaved","surfer","samson","kelly","paul","mine","king","racing","5555","eagle","hentai","newyork","little","redwings","smith","sticky","cocacola","animal","broncos","private","skippy","marvin","blondes","enjoy","girl","apollo","parker","qwert","time","sydney","women","voodoo","magnum","juice","abgrtyu","777777","dreams","maxwell","music","rush2112","russia","scorpion","rebecca","tester","mistress","phantom","billy","6666","albert");
  // Update the password strength meter
  console.log(val)
  let meter_value; 
  $.ajax({
    type: "GET",
    url: `/checkPassword?pass=${escape(val)}`, 
    success:function(data){
      let parsed= JSON.parse(data)
      console.log(val)
      console.log(parsed)
      if (parseFloat(parsed['data'][0]) < 0.20 && parseFloat(parsed['data'][0]) >= 0){
        meter_value = 0
      } 
      else if (parseFloat(parsed['data'][0]) < 0.44 && parseFloat(parsed['data'][0]) >= 0.20){
        meter_value = 1
      }
      else if (parseFloat(parsed['data'][0]) < 0.61 && parseFloat(parsed['data'][0]) >= 0.44){
        meter_value = 2
      }
      else if (parseFloat(parsed['data'][0]) < 0.8 && parseFloat(parsed['data'][0]) >= 0.61){
        meter_value = 3
      } else{
        meter_value = 4
      }
      let requirements = eval(parsed['data'][1])
      console.log(requirements.length)
      if(requirements.length != 0){
        meter_value = 1;
        regsiterbtn.disabled = true
      } 
      else if (meter_value < 2){
        regsiterbtn.disabled = true
      }
      else{
        regsiterbtn.disabled = false
      }
      console.log(meter_value)
      meter.value = meter_value
      if (val !== "") {
        text.innerHTML = "Strength: " + strength[meter_value]; 
        requirements.forEach(ele => {
          if(ele == "Length(8)"){
            text.innerHTML += "<br><span style=color:red>Minimum length of 8 required</span>"
          }
          if (ele == "Uppercase(2)"){
            text.innerHTML += "<br><span style=color:red>Minimum of two uppercases characters requried</span>"
          }
          if (ele == "Numbers(2)"){
            text.innerHTML += "<br><span style=color:red>Minimum of two numbers requried</span>"
          }
          if (ele == "Special(2)"){
            text.innerHTML += "<br><span style=color:red>Minimum of two special characters requried</span>"
          }
          if (ele == "Nonletters(2)"){
            text.innerHTML += "<br><span style=color:red>Minimum of two non-letters characters requried</span>"
          }
        })
      } else {
        text.innerHTML = "";
      }
    }
  })
  // Update the text indicator
});



