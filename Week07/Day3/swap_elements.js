'use strict';
// - Create a variable named `abc` with the following content: `["Arthur", "Boe", "Chloe"]`
// - Swap the first and the third element of `abc`

let abc = ["Arthur", "Boe", "Chloe"]
let tempAbc = abc
abc = [tempAbc[2], tempAbc[1], tempAbc[0]]


console.log(abc)