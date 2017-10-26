  // <!-- You can work in the html or in a separate js file. Like:
  // <script>
  //   1) replace the list items' content with items from this list:
  //   ['apple', 'banana', 'cat', 'dog']
  //   2) change the <ul> element's background color to 'limegreen'
  //     - don't just add a CSS class
  //     - use the .style attribute
  // </script>

let newList = ['apple', 'banana', 'cat', 'dog']

for (i = 0; i < newList.length; i++) {
  document.getElementsByTagName('li')[i].innerText = newList[i]
}

document.getElementsByTagName('ul')[0].style.background = 'limegreen'
