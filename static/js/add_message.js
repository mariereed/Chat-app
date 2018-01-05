"use strict";

$('document').ready(function() {
    function updateFeed(results) {
        // Add the message to the bottom of the feed
        console.log("i made it into the updateFeed function");
        if (! results.message.includes("<script")) {
            var newPar = document.createElement("p");
            newPar.innerText = results.message + ' -- ' + results.author;
            $('.feed').append(newPar);
            var objDiv = document.getElementById("feed");
            objDiv.scrollTop = objDiv.scrollHeight;
        }
        else {
            alert("No XSS please :)");
        }
        $('#formMessage').val('');
    }
    
    function addMessage(evt) {
        evt.preventDefault();
        console.log("i made it into the addMessage function");
        $.post('/add_message', {'message': $('#formMessage').val()}, updateFeed);
    }

    $('.add').on('click', addMessage);
    var objDiv = document.getElementById("feed");
    objDiv.scrollTop = objDiv.scrollHeight;
});
console.log("i made it into the js fieeele");