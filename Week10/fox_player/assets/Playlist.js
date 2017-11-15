'use strickt'

const playlistContainer = document.querySelector('.playlists')
// const listOplaylists = ['All tracks', 'Favourites', 'Worst of the 90s']

let listPlaylist = function(){
    ajax('GET', 'playlists.json', addPlaylist)
}

let addPlaylist = function(list) {
    list.forEach(function(playlist){
        let contentPlaylist = `${playlist.title}`
        let Playlist = document.createElement('li')
        if (playlist.system !== 1) {
            let button = `<button class="delete"></button>`
            Playlist.innerHTML = contentPlaylist + button
        }
        else {
            Playlist.innerHTML = contentPlaylist
        }
        playlistContainer.appendChild(Playlist)
    })
}



const deleteButtons = document.getElementsByClassName('delete')

for (let i = 0; i < deleteButtons.length; i++) {
    deleteButtons[i].addEventListener('click', () => {
        console.log('a click!')
    })
}


