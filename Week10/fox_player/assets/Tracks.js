'use strict'

const trackContainer = document.querySelector('.tracks')
// const listOtracks = ['MSI - Bitches', 'Turmion Katilot - Pyrun nyrkki', 'Bloodhound Gang - Um Tiss Um Tiss Um Tiss', 'Britney Spears - Oops I did it again']

let listTracks = function() {
    ajax('GET', '', '/tracks', addTracks)
}

let addTracks = function(listOtracks) {
    listOtracks.forEach(function(track){
        let element = document.createElement('li')
        element.innerHTML = track.author + ' - ' + track.track_name
        trackContainer.appendChild(element)
    })
}
