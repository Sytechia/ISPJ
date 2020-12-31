function openNav() {
    document.getElementById("mySidebar").style.width = "200px";
    document.getElementById("main").style.marginLeft = "200px";
    }
    function openChat() {
    document.getElementById("myForm").style.width = "400px";
    document.getElementById("main").style.marginLeft = "200px";
    }
    
    function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    }
    function closeChat() {
    document.getElementById("myForm").style.display = "none";
    //document.getElementById("main").style.marginLeft= "0";
    }
    
    function openForm() {
    document.getElementById("myForm").style.display = "block";
    }
    
    function closeForm() {
    document.getElementById("myForm").style.display = "none";
    }
    var chat = document.getElementById("chat");
    chat.scrollTop = chat.scrollHeight - chat.clientHeight;
    
    
    function loadDoc() {
      var fields = $( ":input" ).serializeArray();
    
      $( "#results" ).empty();
      jQuery.each( fields, function( i, field ) {
        //$( "#results" ).append( field.value + " " );
        $.post("/result", {
      javascript_data: field.value+" "
    });
      });
      // TODO: The rest of the code will go here...
    }
    
    window.onload=function () {
         var objDiv = document.getElementById("chat");
         objDiv.scrollTop = objDiv.scrollHeight;
    }
    // messageBody.lastChild.scrollIntoView()
    
    // $("#mydiv").scrollTop($("#chat")[0].scrollHeight);
      
    
    function refreshMessages() {
    $.ajax({
      url: '/',
      type: 'GET',
      dataType: 'html',
      success: function(data) {
        console.log(data)
        $('#chat').html(data); // data came back ok, so display it                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              $('#chat').html(data); // data came back ok, so display it
      },
      error: function() {
        $('#chat').prepend('Error retrieving new messages..');
      }
    });
    }
    
    function replaceLinks(){ 
      let parent = document.querySelector('#chat')
      Array.from(parent.children).forEach(element=> {
        // console.log(element.innerHTML)
        if(element.innerHTML.includes('http') && element.innerHTML.indexOf('png') == -1 && element.innerHTML.indexOf('jpeg') == -1 && element.innerHTML.indexOf('jpg') == -1){
          let str;
          let starting = element.innerHTML.indexOf(':')
          // slice the link 
          str = element.innerHTML.slice(starting+2)
          let malformed = `<a href = ${str}>${str}</a>`
          // slice from the beginning up to the link/colon 
          let orginal = element.innerHTML.slice(0, starting+2)
          orginal += malformed
          console.log(orginal)
          element.innerHTML = orginal
        }
      })
    }
    
    replaceLinks()