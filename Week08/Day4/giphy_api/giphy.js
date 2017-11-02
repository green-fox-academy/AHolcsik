'use strict'


let displayDiv = document.querySelector ('container')

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
        for (let i = 0; i < 16; i++) {
            let newImg = document.createElement('img')
            let toDisplay = gifData.data[i].images.fixed_height_still.url
            newImg.setAttribute('src', toDisplay)
            document.body.insertAdjacentElement('beforeend', newImg)
        }
    }

window.onload = function () {
    getGif (displayGif);
}
