'use strict'

function getGif (callback) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://api.giphy.com/v1/gifs/search?api_key=qgbcFlGRFhawbL3ndpdr6PXddqaDv7DF&q=gravity falls, bill cipher&limit=16&offset=0&rating=PG-13&lang=en');
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
        let containerDiv = document.getElementsByClassName('container')[0]
        let newImg = document.createElement('img')
        let toDisplay = gifData.data[i].images.fixed_width_still.url
        let movingGif = gifData.data[i].images.fixed_width.url
        newImg.setAttribute('src', toDisplay)
        containerDiv.appendChild(newImg)
        let allGifs = document.querySelectorAll('img')
        allGifs[i].addEventListener('click', function() {
            newImg.setAttribute('src', movingGif)})
        }
    }

window.onload = function () {
    getGif (displayGif);
}
