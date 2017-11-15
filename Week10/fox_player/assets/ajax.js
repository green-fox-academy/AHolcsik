'use strict'


function ajax(method, data, url, callback) {
    let xhr = new XMLHttpRequest()
    data = data ? data : null;
    xhr.open(method, url)
    xhr.setRequestHeader('Content-Type', 'application/json')
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            let recievedData = JSON.parse(xhr.responseText)
            callback(recievedData)
        }
    }
    xhr.send()
}

