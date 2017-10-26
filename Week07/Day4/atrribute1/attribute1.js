
//   <!-- You can work in the html or in a separate js file. Like:
//   <script>
//     Write the image's url to the console.
//     Replace the image with a picture of your favorite animal.
//     Make the link point to the Green Fox Academy website.
//     Disable the second button.
//     Replace its text with 'Don't click me!'.
//   </script>

let imgUrl = document.getElementsByTagName('img')[0]
console.log(imgUrl.getAttribute('src'))

imgUrl.setAttribute('src', 'https://i.pinimg.com/236x/48/4f/ab/484fab8d99dba8ad7ebd300e5bd889c7--ghosts-beautiful-creatures.jpg')

document.getElementsByTagName('a')[0].setAttribute('href', 'https://www.greenfoxacademy.com/')

let secondButt = document.getElementsByClassName('this-one')[0]
secondButt.disabled = true
secondButt.textContent = "Don't click me!"


