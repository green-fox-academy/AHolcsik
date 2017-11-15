'use strict'

const trackContainer = document.querySelector('.tracks')
const listOtracks = ['MSI - Bitches', 'Turmion Katilot - Pyrun nyrkki', 'Bloodhound Gang - Um Tiss Um Tiss Um Tiss', 'Britney Spears - Oops I did it again']

let addTracks = function() {
    Tracks.forEach(function(track){
        let element = document.createElement('li')
        element.innerHTML = track
        console.log(element)
        trackContainer.appendChild(element)
    })
}()
