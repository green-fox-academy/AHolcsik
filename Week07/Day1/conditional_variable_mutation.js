'use strict';

var a = 24;
var out = 0;
// if a is even increment out by one

if (a % 2 === 0) {
    out ++;
}

console.log(out);




var b = 3;
var out2 = '';
// if b is between 10 and 20 set out2 to "Sweet!"
// if less than 10 set out2 to "More!",
// if more than 20 set out2 to "Less!"

if (10 < b && b < 20) {
    out2 = 'Sweet!';
} else if (b < 10) {
    out2 = 'More!';
} else if (20 < b) {
    out2 = 'Less!';
}

console.log(out2);



var c = 123;
var credits = 220;
var isBonus = true;
// if credits are at least 50,
// and is_bonus is false decrement c by 2
// if credits are smaller than 50,
// and is_bonus is false decrement c by 1
// if is_bonus is true c should remain the same

if (isBonus == false) {
    if (credits >= 50) {
        c -= 2;
    } else if (credits < 50) {
        c -= 1;
    } 
}

console.log(c);




let d = 9;
let time = 1000;
let out3 = '';
// if d is dividable by 4
// and time is not more than 200
// set out3 to "check"
// if time is more than 200
// set out3 to "Time out"
// otherwise set out3 to "Run Forest Run!"

if (d % 4 === 0) {
    if (time <= 200) {
        out3 = 'check';
    } else {
        out3 = 'time out';
    }
} else {
    out3 = 'Run Forest Run!';
}

console.log(out3);