'use strict';
// - Create a function called `printer`
//   which logs to the console the input parameters
//   (can have multiple number of arguments)

function printer () {
    let args = arguments
    for (let i = 0; i < args.length; i++) {
        console.log(args[i]);
    }
}

printer('pony', 'kitten', 'marmaduke')