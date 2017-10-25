'use strict';

let example = "In a dishwasher far far away";

// I would like to replace "dishwasher" with "galaxy" in this example
// Please fix it for me!
// Expected ouput: In a galaxy far far away


console.log(example.replace(/dishwasher/g, 'galaxy'));
console.log(example.split('dishwasher').join('galaxy'));

