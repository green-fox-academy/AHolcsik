'use strict';

function factorialTillLimitWithCallback(limit, callback) {
  var factorial = 1;
  for (var i = 1; i <= limit; ++i) {
    callback(factorial);
    // console.log(callback)
    factorial *= i;
  }
}

let call = function(factorial) {
    console.log(factorial)
}

// Create a function and pass it as a parameter to the factorialTillLimitWithCallback
// function, and print all the factorial numbers till 20

factorialTillLimitWithCallback(20, call)