
'use strict';

let currentHours = 14;
let currentMinutes = 34;
let currentSeconds = 42;

// Write a program that prints the remaining seconds (as an integer) from a
// day if the current time is represented by these variables

function remaining_seconds () {
    let all_seconds = 24 * 60 * 60;
    console.log(all_seconds - currentHours * 3600 - currentMinutes * 60 - currentSeconds);
}

remaining_seconds()