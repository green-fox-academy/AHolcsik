'use strict'

const playlistContainer = document.querySelector('.playlists')
const trackContainer = document.querySelector('.tracks')
const listOplaylists = ['All tracks', 'Favourites']
const listOtracks = ['MSI - Bitches', 'Turmion Katilot - Pyrun nyrkki', 'Bloodhound Gang - Um Tiss Um Tiss Um Tiss', 'Britney Spears - Oops I did it again']

let addPlaylist = function() {
    listOplaylists.forEach(function(playlist){
        let them = document.createElement('li')
        them.innerHTML = playlist
        playlistContainer.appendChild(them)
    })
}()

let addTracks = function() {
    listOtracks.forEach(function(track){
        let element = document.createElement('li')
        element.innerHTML = track
        console.log(element)
        trackContainer.appendChild(element)
    })
}()