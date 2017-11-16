'use strict'

const playlistContainer = document.querySelector('.playlists')

let listPlaylist = function(){
    ajax('GET', '', '/playlists', addPlaylist)
}

let addPlaylist = function(list) {
    playlistContainer.innerHTML = ''
    list.forEach(function(playlist){
        let contentPlaylist = `${playlist.playlist}`
        let Playlist = document.createElement('li')
        Playlist.setAttribute('class', 'playlist')
        if (playlist.system !== 1) {
            let button = `<button id="${playlist.id}" class="delete"></button>`
            Playlist.innerHTML = contentPlaylist + button
        }
        else {
            Playlist.innerHTML = contentPlaylist
        }
        playlistContainer.appendChild(Playlist)
    })
    setEventlistenersPlaylists()
}

function setEventlistenersPlaylists() {
    const deleteButtons = document.getElementsByClassName('delete')
    const playlistElements = document.querySelectorAll('.playlist')

    for (let i = 0; i < deleteButtons.length; i++) {
        deleteButtons[i].addEventListener('click', function(){
            let id = {'id': deleteButtons[i].getAttribute('id')}
            deletePlaylist(id)
        })
    }

    playlistElements.forEach(function(e){
        e.addEventListener('click', () => {
            playlistElements.forEach( e => e.classList.remove('active'))
                e.classList.add('active')
        })
    })
}

const addButton = document.querySelector('.add')

addButton.addEventListener('click', function(){
    let inputBox = document.createElement('article')
    let inputField = `<input type="text" placeholder="enter playlist">
                      <button class="okay">OK</button> <button class="cancel">cancel</button>`
    inputBox.innerHTML = inputField
    document.querySelector('body').appendChild(inputBox)

    let userInput = document.querySelector('input')
    
    document.querySelector('.okay').addEventListener('click', function(){
        let data = {'playlist': userInput.value}
        ajax('POST', data, '/playlists', listPlaylist)
        document.querySelector('body').removeChild(inputBox)
    })
})

function deletePlaylist(id){
    ajax('DELETE', id, '/playlists', listPlaylist)
}
