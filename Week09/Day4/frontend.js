'use strict';

const url = 'http://localhost:8080';
const displayArticle = document.querySelector('article')


const ajax = function(method, callback) {
    const xhr = new XMLHttpRequest();
    console.log('ajax try')
    xhr.open (method, url)
    xhr.setRequestHeader('Content-Type', 'application/json')
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            console.log(JSON.parse(xhr.response))
            callback (JSON.parse(xhr.response))
        }
    }
    xhr.send()
}

var getBookNames = function(callback) {
    console.log('this worked')
    ajax('GET', callback)
}

var displayBookNames = function(data) {
    data.forEach(function(book){
        console.log('this tried it too')
        const Books = document.createElement('li')
        displayedBook.innerText = book.name
        displayArticle.appendChild(displayedBook)
    })
}

getBookNames(displayBookNames);

