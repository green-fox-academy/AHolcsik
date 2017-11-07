let test = require('tape');
var getApple = require('./apples');

test('return apple', function (t) {
  t.equal(getApple, 'apple');
  t.end();
});