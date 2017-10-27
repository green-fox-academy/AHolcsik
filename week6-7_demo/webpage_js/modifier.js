
// window.addEventListener('scroll', tellMe)


// function tellMe () {
//   if (window.scrollY > 300) {
//     console.log('O MY GAWD');
//   }
// }

let nav = document.getElementsByTagName('nav')[0];

window.addEventListener('scroll', makeFixed)

function makeFixed () {
  if (window.scrollY > 450) {
    nav.setAttribute ('class', 'fixed');
  } else if (window.scrollY < 450) {
    nav.removeAttribute ('class', 'fixed')
  }
}


