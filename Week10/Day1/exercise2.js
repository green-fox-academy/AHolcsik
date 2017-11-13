'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference


const createRectangle = function () {

    const getArea = function (a, b) {
        console.log (a * b)
    }

    const getCircumference = function (a, b) {
        console.log (2 * (a + b))
    }

    return {
        getArea : getArea,
        getCircumference : getCircumference
    }
}

const square = createRectangle()
square.getArea(4, 4)
const rectangle = createRectangle()
rectangle.getCircumference(20, 5)
