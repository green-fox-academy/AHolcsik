'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

const createAnimal = function () {

    const say = function (sound) {
        console.log (sound)
    }

    return {
        say : say
    }
}

const dog = createAnimal()
dog.say('vau')
const pony = createAnimal()
dog.say('neigh!')