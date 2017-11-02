'use strict'


let displayDiv = document.querySelector ('img')

function getGif (callback) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://api.giphy.com/v1/gifs/search?api_key=qgbcFlGRFhawbL3ndpdr6PXddqaDv7DF&q=gravity falls&limit=16&offset=0&rating=PG-13&lang=en');
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            let Gifs = JSON.parse(xhr.responseText)
            callback (Gifs)
        }
    }
    xhr.send()
}

function displayGif(gifData) {
    let toDisplay = gifData.data[9].images.original.url
    console.log(toDisplay)
    displayDiv.setAttribute('src', toDisplay)
}


window.onload = function () {
    getGif (displayGif);
}
