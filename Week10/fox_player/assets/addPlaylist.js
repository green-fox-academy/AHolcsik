'use strickt'

const playlistContainer = document.querySelector('.playlists')
const listOplaylists = ['All tracks', 'Favourites']

let addPlaylist = function() {
    listOplaylists.forEach(function(playlist){
        let them = document.createElement('li')
        them.innerHTML = playlist
        playlistContainer.appendChild(them)
    })
}()