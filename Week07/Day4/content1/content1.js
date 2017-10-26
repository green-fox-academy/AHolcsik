//  <!-- You can work in the html or in a separate js file. Like:

//   <script>
//     1. Alert the content of the heading.

//     2. Write the content of the first paragraph to the console.

//     3. Alert the content of the second paragraph.

//     4. Replace the heading's content with 'New content'.

//     5. Replace the last paragraph's content with the first paragraph's content.

//   </script>



let heading = document.querySelector('h1').textContent
alert(heading)

let paragraph = document.getElementsByTagName('p')
console.log(paragraph[0].textContent)

alert(paragraph[1].textContent)

document.querySelector('h1').innerHTML = 'New content'

document.getElementsByTagName('p')[2].innerHTML = paragraph[0].textContent

