
$(document).ready(function () {
    var siriWave = new SiriWave({
        container: document.getElementById('siri-container'),
        width: 640,
        height: 200,
        style: "ios9",
        amplitude: 2.3,
        speed: 0.16,
        autostart: true
    });

  
    $('.siri-message').textillate({
        loop: true,               
        minDisplayTime: 2000,     
        initialDelay: 0,          
        autoStart: true,          
        in: {
            effect: "fadeInUp",   
            sync: true,           
        },
        out: {
            effect: "fadeOutUp",  
            sync: true,           
        }
    });

    //mic button click event 

    $("#MicButton").click(function () { 
        
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands()
        
    });

    function doc_key(e) {
        const isCmdOrCtrl = e.metaKey || e.ctrlKey; 
        const key = (e.key || "").toLowerCase();
        if (isCmdOrCtrl && key === "k") {          
          e.preventDefault();
          $("#Oval").attr("hidden", true);
          $("#SiriWave").attr("hidden", false);
          eel.allCommands();                       
        }
      }
      window.addEventListener("keydown", doc_key, false);
    });



