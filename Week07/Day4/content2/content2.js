
//   <!-- You can work in the html or in a separate js file. Like:
//   <script>
//     fill every paragraph with the last one's content.
//   </script>
  
let paragraphs = document.getElementsByTagName('p')

for (p = 0; p <= paragraphs.length; p++) {
    document.getElementsByTagName('p')[p].innerHTML = paragraphs[3].textContent
}


