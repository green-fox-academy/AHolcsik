'use strict'

let btn = document.querySelector('button')

function getArticle () {
    let xhr = new XMLHttpRequest();
    xhr.open ('GET', 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=1fc7a7dbfaee49a7b9012a13b9bee39b&begin_date=19690719&end_date=19690720')
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            let Article = JSON.parse(xhr.responseText)
            console.log(Article)
        }
    }
    xhr.send()
}

getArticle()

btn.addEventListener('click', function () {
    document.location.href = '!!link goes here!!'
})




// function getFilm ( id, callback ) {
//     let xhr = new XMLHttpRequest();
//     xhr.open('GET','https://swapi.co/api/films/'+id+'/?format=json');
//     xhr.onreadystatechange = function() {
//         if(xhr.readyState == 4) {
//             let films = JSON.parse(xhr.responseText)
//             callback( films );
//         }
//     }
//     xhr.send()
// }

// function showDetails( filmData ) {
//     console.log( filmData.title )
// }

// function renderMovie( filmData ) {
//     let h1 = document.createElement('h1');
//     h1.textContent = filmData.title
//     document.body.appendChild(h1)
// }

// document.querySelector('button').addEventListener('click',function(){
//     getFilm(2, renderMovie );
// })




