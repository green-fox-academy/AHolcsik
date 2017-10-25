
'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

function factorio (number) {
    let result = number;
    for (let i = number - 1; i > 0; i--) {
        result = result * i;
    } return result;
}

console.log(factorio (5))