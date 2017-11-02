'use strict'

let btn = document.querySelector('button')
let containerDiv = document.getElementsByClassName('container')[0]


function getArticle (callback) {
    let xhr = new XMLHttpRequest();
    xhr.open ('GET', 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=1fc7a7dbfaee49a7b9012a13b9bee39b&begin_date=19690719&end_date=19690720')
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            let Article = JSON.parse(xhr.responseText).response.docs
            console.log(Article)
            Article.forEach (callback)
        }
    }
    xhr.send()
}

function displayArticle (articleData) {
    let newUl = document.createElement('ul')
    let newHeadline = document.createElement('li')
    let newSnippet = document.createElement('li')
    let newDate = document.createElement('li')
    newHeadline.textContent = 'Headline :' + articleData.headline.main
    newSnippet.textContent = articleData.snippet
    newDate.textContent = articleData.pub_date
    console.log(newHeadline)
    console.log(newSnippet)
    containerDiv.appendChild(newUl)
    newUl.appendChild(newHeadline)
    newUl.appendChild(newSnippet)
    newUl.appendChild(newDate)
    


}


// btn.addEventListener('click', function () {
//     document.location.href = '!!link goes here!!'
// })


window.onload = function () {
    getArticle (displayArticle);
}

{/* <button>Click me for a cool article</button> */}




