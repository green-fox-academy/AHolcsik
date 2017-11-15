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


// let myBut = document.getElementsByTagName('button')[0]
// let url = 'https://api.giphy.com/v1/gifs/search?api_key=qgbcFlGRFhawbL3ndpdr6PXddqaDv7DF&'
// let mySecondBut = document.getElementsByTagName('button')[1]
// myBut.addEventListener("click", click)

// function getGif (searchUrl, callback) {
//     let xhr = new XMLHttpRequest();
//     console.log(searchUrl)
//     xhr.open('GET', url + searchUrl);
//     console.log(url + searchUrl)
//     xhr.setRequestHeader('Content-Type', 'application/json')
//     xhr.onreadystatechange = function() {
//         if (xhr.readyState == 4) {
//             let Gifs = JSON.parse(xhr.responseText)
//             console.log(Gifs)
//             callback (Gifs)
//         }
//     }
//     xhr.send()
// }

// function displayGif(gifData) {
//     for (let i = 0; i < 12; i++) {
//         let containerDiv = document.getElementsByClassName('container')[0]
//         let newImg = document.createElement('img')
//         let toDisplay = gifData.data[i].images.fixed_width_still.url
//         let movingGif = gifData.data[i].images.fixed_width.url
//         newImg.setAttribute('src', toDisplay)
//         containerDiv.appendChild(newImg)

//         let allGifs = document.querySelectorAll('img')
//         allGifs[i].addEventListener('click', function() {
//             newImg.setAttribute('src', movingGif)})
        
//         let madness = function (){
//             allGifs.forEach(function(gif) {
//                 newImg.setAttribute('src', movingGif)
//             });
//         }

//         mySecondBut.addEventListener ('click', madness)
        
//         }
//     }


// function click() {
//     let searchInput = document.getElementById('mySearch').value;
//     let searchUrl = 'q=' + searchInput + '&limit=16&offset=25&rating=PG-13&lang=en'
//     if (searchInput !== "") {
//         getGif (searchUrl, displayGif);
//     }
//     else {
//         let warning = document.createElement('h5')
//         warning.innerHTML = 'nothing to search'
//         document.body.appendChild(warning)
//     }
// }
