'use strict';

const url = 'http://localhost:3000';


const ajax = function(callback) {
    const xhr = new XMLHttpRequest();
    xhr.open ('GET', url)
    xhr.setRequestHeader('Content-Type', 'application/json')
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            console.log(JSON.parse(xhr.response))
            callback (JSON.parse(xhr.response))
        }
    }
}

var getBookNames = function(callback) {

}

var displayBookNames = function(callback) {

}

getBookNames(displayBookNames);
