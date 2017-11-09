'use strict';

const url = 'http://localhost:3000';
const displayArticle = document.querySelector('article')


const ajax = function(method, callback) {
    const xhr = new XMLHttpRequest();
    xhr.open (method, url)
    xhr.setRequestHeader('Content-Type', 'application/json')
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            console.log(JSON.parse(xhr.response))
            callback (JSON.parse(xhr.response))
        }
    }
}

var getBookNames = function(callback) {
    ajax('GET', callback)
}

var displayBookNames = function(data) {
    data.forEach(function(book){
        const Books = document.createElement('li')
        displayedBook.innerText = book.name
        displayArticle.appendChild(displayedBook)
    })
}

getBookNames(displayBookNames);

