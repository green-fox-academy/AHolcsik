let test = require('tape');
let sum = require('./sum');

test('return apple', function (t) {
  t.equal(sum, 'apple');
  t.end();
});