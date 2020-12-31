//Opening of tabs and setting color of the tab to the current one the user is on 
function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}

let tablinks = document.getElementsByClassName("btn");
Array.from(tablinks).forEach(iter => {
    iter.addEventListener('click', event => {
        Array.from(tablinks).forEach(i => {
            i.style.backgroundColor = ''
        })
        event.target.style.backgroundColor = '#0E4D40'
        event.target.style.border = '1 px solid #d4af37'
        
    })
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
    // if (e.target.style.transform === 'rotate(225deg)') {
    //     e.target.style.transform = 'rotate(45deg)';
    // } else {
    //     e.target.style.transform = 'rotate(225deg)';
    // }
})

//Single-Product Zoom in and expand
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


//My account view and update tab
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

//Review carrousell
var slides = document.getElementsByClassName("mySlides")
if(slides) {
    var slideIndex = 1;
    showSlides(slideIndex);

    function plusSlides(n) {
        showSlides(slideIndex += n);
    }

    function currentSlides(n) {
        showSlides(slideIndex = n);
    }

    function showSlides(n) {
        var i;
        var slides = document.getElementsByClassName("mySlides");
        var dots = document.getElementsByClassName("dot");
        if (n > slides.length) {
            slideIndex = 1
        }    
        if (n < 1) {
            slideIndex = slides.length
        }
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";  
        }
        for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
        }
        slides[slideIndex-1].style.display = "block";  
        dots[slideIndex-1].className += " active";
        }
}