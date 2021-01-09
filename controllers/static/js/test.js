const SpeechRecognition = window.speechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();

recognition.onstart = function() {
    console.log('voice is activated, you can use the microphone')
}

recognition.onresult = function(event) {
    const current = event.resultIndex;
    const transcript = event.results[current][0].transcript
    console.log(transcript)
    document.querySelector('input[name="msg"]').value = transcript
    document.querySelector('#out').click()
}

const mic = document.querySelector('#mic')
console.log(mic)

$('#mic').on('click', mic,()=> {
    console.log('fired')
    recognition.start()
})

Swal.fire({
    title: 'Do you want to hear the AI?',
    showDenyButton: true,
    confirmButtonText: `Yes`,
    denyButtonText: `No`,
  }).then((result) => {
    /* Read more about isConfirmed, isDenied below */
    if (result.isConfirmed) {
        $.ajax({
            "type":"GET",
            "url":"/latest",
            success: function(data){
                let malformed = eval(data)
                console.log(malformed)
                // document.querySelector('.hide').click();
                Array.from(malformed).forEach(element => {
                    document.querySelector('.hide').click();
                    var timer = setInterval(function() {
                        voices = speechSynthesis.getVoices();
                        console.log(voices);
                        if (voices.length !== 0) {
                            msg = new SpeechSynthesisUtterance(element);
                            msg.voice = voices[4];
                            speechSynthesis.cancel();
                            speechSynthesis.speak(msg);
                            msg.lang = 'en-US';
                            clearInterval(timer);
                        }
                    }, 200);
                })
            }
        })
    } else if (result.isDenied) {
      Swal.fire('No voice will be relayed to you', '', 'info')
    }
  })



$.ajax({
    "type":"GET",
    "url":"/latest",
    success: function(data){
        let malformed = eval(data)
        console.log(malformed)
        var bool;
        // document.querySelector('.hide').click();
        Array.from(malformed).forEach(element => {
          console.log(element == "We have three different shipping options, express delivery, postal mail and standard delivery. The prices vary according to the weight of your package and your shipping options. For more information, please refer to shipping fee table on the faq page.")
          if(element == "We have three different shipping options, express delivery, postal mail and standard delivery. The prices vary according to the weight of your package and your shipping options. For more information, please refer to shipping fee table on the faq page."){
            document.querySelector('#fee').setAttribute('open','')
            bool = true
            console.log('here')
          }
    })
    function findPos(obj) {
                var curtop = 0;
                if (obj.offsetParent) {
                    do {
                        curtop += obj.offsetTop;
                    } while (obj = obj.offsetParent);
                return [curtop];
                }
            }
    if(bool){
    window.scroll(0,findPos(document.getElementById("fee")));
    }
}
    })