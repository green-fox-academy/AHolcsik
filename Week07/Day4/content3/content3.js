
//   <!-- You can work in the html or in a separate js file. Like:
//   <script>
//     fill output1 with the first paragraph's content, text only.
//     fill output2 with the first paragraph's content keeping the cat strong.
//   </script>
//   OR

document.querySelector('.output1').innerHTML = document.getElementsByTagName('p')[0].textContent

document.querySelector('.output2').innerHTML = document.getElementsByTagName('p')[0].innerHTML

