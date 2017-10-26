'use strict';
// Join the two array by matching one girl with one boy in the order array
// Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

var girls = ["Eve","Ashley","Bözsi","Kat","Jane"];
var boys = ["Joe","Fred","Béla","Todd","Neef","Jeff"];
var order = [];

// for (let i = 0; i < girls.length; i++) {
//     for (let j = 0; j < boys.length; j++) {
//         if (i === j) {
//             order.push(girls[i]);
//             order.push(boys[j])
//             // + Jeff
//         }
//     }
// }

// console.log(order);

order = boys
for (let i = 0; i < girls.length; i++) {
        order.splice(i+2, 0, girls[i]);
            }

console.log(order);

