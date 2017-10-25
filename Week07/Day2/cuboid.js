'use strict';

// Write a program that stores 3 sides of a cuboid as variables (floats)
// The program should write the surface area and volume of the cuboid like:
//
// Surface Area: 600
// Volume: 1000

function cubiod (a, b, c) {
    console.log ('Surface Area: ' + (a * b) + (b * c) + (a * c) );
    console.log ('Volume: ' + a * b * c);
}
cubiod (4, 6, 10);