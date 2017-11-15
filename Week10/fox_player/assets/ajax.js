'use strict'

const url = 'tracks.json'

function ajax(callback) {
    let xhr = new XMLHttpRequest()
    xhr.open('GET', url)
    xhr.setRequestHeader('Content-Type', 'application/json')
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            let recievedData = JSON.parse(xhr.responseText)
            callback(recievedData)
        }
    }
    xhr.send()
}

ajax()
