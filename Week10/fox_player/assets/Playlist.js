'use strickt'

const playlistContainer = document.querySelector('.playlists')
const listOplaylists = ['All tracks', 'Favourites', 'Worst of the 90s']

let addPlaylist = function() {
    listOplaylists.forEach(function(playlist){
        let contentPlaylist = `${playlist}`
        let Playlist = document.createElement('li')
        // dinamic variable will decide this part
        if (playlist !== 'All tracks', 'Favourites') {
            let button = `<button class="delete"></button>`
            Playlist.innerHTML = contentPlaylist + button
        }
        else {
            Playlist.innerHTML = contentPlaylist
        }
        playlistContainer.appendChild(Playlist)
    })
}()



