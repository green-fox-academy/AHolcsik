'use strict';

const url = 'http://localhost:8080';
const displayArticle = document.getElementsByTagName('article')[0]


const ajax = function(method, endpoint, callback) {
    const xhr = new XMLHttpRequest();
    console.log(url+endpoint)
    xhr.open (method, url + endpoint)
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
    console.log('is get')
    ajax('GET', 'bookstore', callback)
}

var displayBookNames = function(data) {
    data.forEach(function(book){
        console.log(book.name)
        const Books = document.createElement('li')
        displayedBook.innerText = book.name
        displayArticle.appendChild(displayedBook)
    })
}
console.log('maybe this')
getBookNames(displayBookNames);

