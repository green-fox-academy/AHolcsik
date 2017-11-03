'use strict'

function getPosts (callback) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://cors-anywhere.herokuapp.com/http://secure-reddit.herokuapp.com/posts')
    xhr.onload = function() {
        JSON.parse(xhr.response).posts.forEach (callback)
    }
    xhr.send()
}

function displayData(data) {

    console.log(data)
}

getPosts(displayData)
