let dates = document.querySelectorAll('.tran_date');
let datee = document.querySelectorAll('.trans_date');

// (()=> {
//   Array.from(dates).forEach(date => {
//     let orginal = date.textContent
//     console.log(date)
//     let adjusted = orginal.slice(0, -7)
//     date.innerText = adjusted
//   })
//   Array.from(datee).forEach(date => {
//     let orginal = date.value
//     console.log(orginal)
//     let adjusted = orginal.slice(0, -7)
//     date.value = adjusted
//   })
// })();
$(".sidebar-dropdown > a").click(function() {
  $(".sidebar-submenu").slideUp(200);
  if (
    $(this)
      .parent()
      .hasClass("active")
  ) {
    $(".sidebar-dropdown").removeClass("active");
    $(this)
      .parent()
      .removeClass("active");
  } else {
    $(".sidebar-dropdown").removeClass("active");
    $(this)
      .next(".sidebar-submenu")
      .slideDown(200);
    $(this)
      .parent()
      .addClass("active");
  }
});

function openTab(evt, cityName) {
  var i, tab_tabcontent, tab_tablinks;
  tab_tabcontent = document.getElementsByClassName("tab_tabcontent");
  for (i = 0; i < tab_tabcontent.length; i++) {
    tab_tabcontent[i].style.display = "none";
  }
  tab_tablinks = document.getElementsByClassName("tab_tablinks");
  for (i = 0; i < tab_tablinks.length; i++) {
    tab_tablinks[i].className = tab_tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}


$('.fa-search-plus').click(event=> {
  const id = event.target.parentElement.children[0].innerText
  window.location.href=`/viewIndividualUser?id=${id}`
})

$('.showOrderDetails').click(e => {
  let childrens = event.target.parentElement.parentElement.parentElement.parentElement.children
  Array.from(childrens).forEach(x => {
      let i = x.children[0].children[0]
      if(i.classList.contains('orderDetails')) {
          if (i.style.display === "none") {
                  i.style.display = "block";
              } else {
                  i.style.display = "none";
              }
      }
  })
  // var y = document.getElementById("arrowStyle");
  // if (y.style.transform === 'rotate(225deg)') {
  //     y.style.transform = 'rotate(45deg)';
  // } else {
  //     y.style.transform = 'rotate(225deg)';
  // }

})

$('.orderStatus').click(event => {
  let ids = event.target.parentElement.parentElement.children[2].children[1].value
  let id = ids.substr(1)
  window.location.href=`/orderStatus?id=${id}`
})

$('.fa-trash-o').click(event => {
  const id = event.target.parentElement.children[0].innerText
  console.log(id)
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
        'User has been deleted.',
        'success'
      )
      event.target.parentElement.parentElement.parentElement.parentElement.remove()    
      $.ajax({
        type: "GET",
        url: `/deleteUser?delete=true&userId=${id}`,
    })
    } else if (
      /* Read more about handling dismissals below */
      result.dismiss === Swal.DismissReason.cancel
    ) {
      swalWithBootstrapButtons.fire(
        'Cancelled',
        'User has not been eliminated yet..',
        'error'
      )
    }
  })
})

