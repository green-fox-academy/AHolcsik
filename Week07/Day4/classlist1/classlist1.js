
//   <!-- You can work in the html or in a separate js file. Like:
//   <script>
//     Does the third p have a red-dot class?
//     If so, alert 'OMG DOTS!'
//     If the fourth p has a 'dolphin' class, replace apple's content with 'pear'
//     If the first p has an 'apple' class, replace cat's content with 'dog'
//     Make apple red by adding a .red class
//     Make balloon less balloon-like
//   </script>
//   OR

let paragraphs = document.getElementsByTagName('p')
let dotted = paragraphs[2].classList.value

if (dotted.includes('dot')) {
    alert('OMG DOTS!')
}

if (paragraphs[3].classList.value.includes('dolphin')) {
    paragraphs[0].setAttribute ('class', 'pear')
}

if (paragraphs[0].classList.value.includes('apple')) {
    paragraphs[2].innerHTML = 'dog'
}

paragraphs[0].className += ' red'

if (paragraphs[1].classList.value.includes('balloon')) {
    paragraphs[1].removeAttribute('class', 'balloon')
}

// console.log(paragraphs[2].classList.value)