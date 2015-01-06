/*
 * Project Home Smart Home
 * Client App index.js
 * Aug 2014
 * Version 1.0
 * (c) Jannis Portmann
 */

var app = {
    // Set position to 0
    var position = 0;

    // Application Constructor
    initialize: function() {
        this.bindEvents();
    },
    // Bind Event Listeners
    //
    // Bind any events that are required on startup. Common events are:
    // 'load', 'deviceready', 'offline', and 'online'.
    bindEvents: function() {
        document.addEventListener('deviceready', this.onDeviceReady, false);
    },
    // deviceready Event Handler
    //
    // The scope of 'this' is the event. In order to call the 'receivedEvent'
    // function, we must explicity call 'app.receivedEvent(...);'
    onDeviceReady: function() {
        app.receivedEvent('deviceready');
        //Check if host is online
        this.checkOnline();
        //Disable back button for navigation
        document.addEventListener('backbutton', onBackKeyDown(), false);
    },
    // Update DOM on a Received Event
    receivedEvent: function(id) {
        var parentElement = document.getElementById(id);
        var listeningElement = parentElement.querySelector('.listening');
        var receivedElement = parentElement.querySelector('.received');

        listeningElement.setAttribute('style', 'display:none;');
        receivedElement.setAttribute('style', 'display:block;');

        console.log('Received Event: ' + id);
    },


    onBackKeyDown: function() {
        navigator.app.exitApp();
    },

    /* checkOnline: function() {
        $.ajax({url: "http://192.168.1.43:8080",
            type: "HEAD",
            timeout:1,
            statusCode: {
                200: function (response) {
                    //Work
                },
                400: function (response) {
                    window.plugins.toast.showLongBottom("There's a problem ith the connection - 400";
                    navigator.app.exitApp();
                },
                0: function (response) {
                    window.plugins.toast.showLongBottom("There's a problem ith the connection - 0";
                    navigator.app.exitApp();
                }              
            }
        });
    } */
};
