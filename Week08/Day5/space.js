'use strict'

let contentDiv = document.getElementsByClassName('content')[0]

function getPosts (callback) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://cors-anywhere.herokuapp.com/http://secure-reddit.herokuapp.com/posts')
    xhr.onload = function() {
        JSON.parse(xhr.response).posts.forEach (callback)
    }
    xhr.send()
}

function displayData(data) {
    let newUl = document.createElement('ul')
    let newTitle = document.createElement('a')
    let newUser = document.createElement('li')
    newTitle.textContent = data.title
    newUser.textContent = data.user
    newTitle.setAttribute('href', data.url)
    contentDiv.appendChild(newUl)
    newUl.appendChild(newTitle)
    newUl.appendChild(newUser)
}

getPosts(displayData)
