'use strict';
// - Create (dynamically*) a two dimensional list
//   with the following matrix**. Use a loop!
//
//   0 0 0 1
//   0 0 1 0
//   0 1 0 0
//   1 0 0 0
//
// - Print this two dimensional list to the console
//
// * size should depend on a variable
// ** Relax, a matrix is just like an array

function leftMatrix (size) {
    let row = []
    for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
            if (j === i) {
                row.push (1)
            } else {
                row.push(0)
            }
        } console.log(row)
        row = []
        }
}

leftMatrix(4)

console.log('')

// for loops can be the same as above

function rightMatrix (size) {
    let row = []
    for (let i = size; i > 0; i--) {
        for (let j = size; j > 0; j--) {
            if (j === i) {
                row.splice (0, 0, 1)
            } else {
                row.splice(0, 0, 0)
            }
        } console.log(row)
        row = []
        }
}

rightMatrix(4)