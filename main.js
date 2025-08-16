$(document).ready(function () {

  eel.expose(DisplayMessage);
  function DisplayMessage(message) {
      $(".siri-message").text(message);   
      $('.siri-message').textillate('start');  
  }

  eel.expose(ShowHood);
  function ShowHood() {
      $("#Oval").attr("hidden", false);
      $("#SiriWave").attr("hidden", true);
  }

  function PlayAssistant(message) {
    if (message != '') {
      $("#Oval").attr("hidden", true);
      $("#SiriWave").attr("hidden", false);
      eel.allCommands(message);
      $("#chatbox").val("");
      $("#MicButton").attr("hidden", false);
      $("#SendButton").attr("hidden", true);
    }
  }

  function ShowHideButton(message = '') {
    if (message.length == 0) {
      $("#MicButton").attr("hidden", false);
      $("#SendButton").attr('hidden', true);
    } else {
      $("#MicButton").attr("hidden", true);
      $("#SendButton").attr("hidden", false);
    }
  }

  $("#SendButton").click(function () {
    let message = $("#chatbox").val();
    PlayAssistant(message);
  });

  $("#chatbox").on('input', function () {
    let message = $(this).val();
    ShowHideButton(message);
  });

  $("#chatbox").on('keypress', function (e) {
    if (e.which == 13) {
      let message = $(this).val();
      PlayAssistant(message);
    }
  });

  ShowHideButton();

});