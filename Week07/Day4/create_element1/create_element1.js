
//   <!-- You can work in the html or in a separate js file. Like:

//   <script>
//     Add an item that says 'The Green Fox' to the asteroid list.

//     Add an item that says 'The Lamplighter' to the asteroid list.

//     Add a heading saying 'I can add elements to the DOM!' to the .container.

//     Add an image, any image, to the container.
//   </script>

let asteoridList = document.getElementsByTagName('ul')

let foxy = document.createElement('li').innerHTML = 'The Green Fox'

asteoridList.appendchild(foxy)
