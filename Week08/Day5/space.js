'use strict'

let contentDiv = document.getElementsByClassName('content')[0]
let currentDate = Date.now()

function getPosts (callback) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://cors-anywhere.herokuapp.com/http://secure-reddit.herokuapp.com/posts')
    xhr.onload = function() {
        JSON.parse(xhr.response).posts.forEach (callback)
    }
    xhr.send()
}

function displayData(data) {
    let date = data.timestamp - currentDate
    let newUl = document.createElement('ul')
    let newTitle = document.createElement('a')
    let newUser = document.createElement('li')
    let newTime = document.createElement('li')
    newTitle.textContent = data.title
    newUser.textContent = data.user
    newTitle.setAttribute('href', data.url)
    newTime.textContent = 'Posted at: '+ new Date (date)
    contentDiv.appendChild(newUl)
    newUl.appendChild(newTitle)
    newUl.appendChild(newUser)
    newUl.appendChild(newTime)
}


getPosts(displayData)
