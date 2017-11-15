'use strickt'

const playlistContainer = document.querySelector('.playlists')

let listPlaylist = function(){
    ajax('GET', 'playlists.json', addPlaylist)
}

let addPlaylist = function(list) {
    list.forEach(function(playlist){
        let contentPlaylist = `${playlist.title}`
        let Playlist = document.createElement('li')
        Playlist.setAttribute('class', 'playlist')
        if (playlist.system !== 1) {
            let button = `<button class="delete"></button>`
            Playlist.innerHTML = contentPlaylist + button
        }
        else {
            Playlist.innerHTML = contentPlaylist
        }
        playlistContainer.appendChild(Playlist)
    })
    setEventlisteners()
}

function setEventlisteners() {
    const deleteButtons = document.getElementsByClassName('delete')
    const playlistElements = document.querySelectorAll('li')
    for (let i = 0; i < deleteButtons.length; i++) {
        deleteButtons[i].addEventListener('click', () => {
            console.log('a click!')
        })
    }
    
    console.log(playlistElements)
    
    playlistElements.forEach(function(e){
        e.addEventListener('click', () => {
            playlistElements.forEach( e => e.classList.remove('active'))
                e.classList.add('active')
        })
    })
}




