'use strict';

// Swap the values of these variables
var a = 123;
var b = 526;

console.log(a);
console.log(b);

function swap () {
    let tempA = a + b;
    b = tempA - b;
    a = tempA - a;
    console.log(a);
    console.log(b);
}

swap ()