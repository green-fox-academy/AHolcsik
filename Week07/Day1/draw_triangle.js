'use strict';

var lineCount = 4;

// Write a program that draws a
// triangle like this:
//
// *
// **
// ***
// ****
//
// The triangle should have as many lines as lineCount is

for (let i = 1; i <= lineCount; i++) {
    let str = ''
    for (let j = i; j = i + 1; j++){
        str += '*'
    }
    console.log(str)
}


