'use strict';

var students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

// create a function that takes a list of students and logs: 
// - how many candies are owned by students

function listStudents () {
    students.forEach(function(kid) {
        console.log(kid.name + ' has ' + kid.candies + ' candies')
    });
}

listStudents(students)
console.log('')

// create a function that takes a list of students and logs:
// - Sum of the age of people who have lass than 5 candies

function sumCandies () {
    let sumAge = 0
    students.forEach(function(kid){
        if (kid.candies >= 5) {
            sumAge += kid.age
        }
    }); console.log('Sum of age of kids who have less than 5 candies: ' + sumAge)
}

sumCandies()