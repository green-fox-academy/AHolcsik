'use strict'

const trackContainer = document.querySelector('.tracks')
const currentContainer = document.querySelector('.current')

let listTracks = function() {
    ajax('GET', '', '/tracks', addTracks)
}

let addTracks = function(listOtracks) {
    listOtracks.forEach(function(track){
        let element = document.createElement('li')
        element.innerHTML = track.path
        trackContainer.appendChild(element)
    })
}

let displayCurrent = function (){
    let current = document.querySelector('audio').getAttribute('src')
    let currentElement = `<article class="playing">${current} is playing</article>`
    currentContainer.innerHTML = currentElement
}()
