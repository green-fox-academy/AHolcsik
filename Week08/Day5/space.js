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
    let newTitle = document.createElement('li')
    let newUser = document.createElement('li')
    // let newDate = document.createElement('li')
    newTitle.textContent = data.title
    newUser.textContent = data.user
    // newDate.textContent = articleData.pub_date
    console.log(newTitle)
    console.log(newUser)
    contentDiv.appendChild(newUl)
    newUl.appendChild(newTitle)
    newUl.appendChild(newUser)
    // newUl.appendChild(newDate)
    console.log(data)
}

getPosts(displayData)
