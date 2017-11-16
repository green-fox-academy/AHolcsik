'use strickt'

const playlistContainer = document.querySelector('.playlists')

let listPlaylist = function(){
    ajax('GET', '', '/playlists', addPlaylist)
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

    playlistElements.forEach(function(e){
        e.addEventListener('click', () => {
            playlistElements.forEach( e => e.classList.remove('active'))
                e.classList.add('active')
        })
    })
}

const addButton = document.querySelector('.add')

addButton.addEventListener('click', function(){
    console.log('yiha!')
    let inputBox = document.createElement('article')
    let inputField = `<input type="text" placeholder="enter playlist">
                      <button class="okay">OK</button> <button class="cancel">cancel</button>`
    inputBox.innerHTML = inputField
    document.querySelector('body').appendChild(inputBox)

    let userInput = document.querySelector('input')
    
    document.querySelector('.okay').addEventListener('click', function(){
        let data = {'title': userInput.value, 'system': 0}
        ajax('POST', data, '/playlists', addPlaylist)
    })
})

