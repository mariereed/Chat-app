"use strict";

$('document').ready(function() {

    // connect to the server through web sockets
    var socket = io.connect('http://127.0.0.1:5000');

    // what to do when a connection event occurs
    socket.on('connect', function() {
        socket.send('User has connected!');
    });

    // what to do when a message event occurs
    socket.on('message', function(msg) {
        $(".feed").append('<li>'+msg+'</li>');
    });

    // what to do when the input button is clicked
    $('.add').on('click', function() {
        socket.send($('#formMessage').val());
        $('#formMessage').val('');
    });



    function updateFeed(results) {
        // Add the message to the bottom of the feed
        console.log("i made it into the updateFeed function");
        var newPar = document.createElement("p");
        newPar.innerText = results.message + ' -- ' + results.author;
        $('.feed').append(newPar);
        var objDiv = document.getElementById("feed");
        objDiv.scrollTop = objDiv.scrollHeight;
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