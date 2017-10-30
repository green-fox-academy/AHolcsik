// Create a Sharpie constructor function

// We should know about each sharpie:
// color (which should be a string)
// width (which will be a number)
// inkAmount (another number)
// When instantiating a Sharpie, we need to specify the color and the width
// Every sharpie is created with a default 100 as inkAmount
// We can use() the sharpie objects
// which decreases inkAmount by the width
// Write a loop that consumes all the sharpie's ink.
// Make sure your loop works with any inkAmount, so your code figures out when it's out of ink.

class sharpie {

    constructor(color, width) {
        this.color = color;
        this.width = width;
        this.inkAmount = 100;
    }

    use() {
        this.inkAmount -= this.width;
    }

    burnAway() {
        console.log(this.inkAmount)
        while (this.inkAmount > 0) {
            this.use();
            console.log(this.inkAmount);
        }
        console.log(this.color + ' sharpie ran out of ink :c')
    }
    
}

let peachpuff = new sharpie ('peachpuff', 20);
peachpuff.burnAway();

