'use strict'

const trackContainer = document.querySelector('.tracks')
const currentContainer = document.querySelector('.current')

let listTracks = function() {
    ajax('GET', '', '/tracks', addTracks)
}

let addTracks = function(listOtracks) {
    listOtracks.forEach(function(track){
        let element = document.createElement('li')
        element.setAttribute('class', 'track')
        element.innerHTML = track.path
        trackContainer.appendChild(element)
    })
    setEventlistenersTracks()
}


let displayCurrent = function (){
    let current = document.querySelector('audio').getAttribute('src')
    let currentElement = `<article class="playing">${current} is playing</article>`
    currentContainer.innerHTML = currentElement
}()

function setEventlistenersTracks() {
    const trackElements = document.querySelectorAll('.track')
    console.log(trackElements)

    trackElements.forEach(function(e){
        e.addEventListener('click', () => {
            trackElements.forEach( e => e.classList.remove('activeTrack'))
                e.classList.add('activeTrack')
        })
    })
}
