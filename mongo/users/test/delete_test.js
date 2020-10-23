const assert = require('assert');
const User = require('../src/models/user.model');

describe('Deleting records', () => {
  let joe;

  beforeEach((done) => {
    joe = new User({ name: 'Joe' });

    joe.save().then(() => {
      done();
    });
  });

  function assertNull(operation, done) {
    operation
      .then(() => User.findOne({ name: 'Joe' }))
      .then((user) => {
        assert(user === null);
        done();
      });
  }

  it('model instance remove', (done) => {
    assertNull(joe.remove(), done);
  });

  it('class method remove', (done) => {
    assertNull(User.remove({ name: 'Joe' }), done);
  });

  it('class method findOneAndRemove', (done) => {
    assertNull(User.findOneAndRemove({ name: 'Joe' }), done);
  });

  it('class method findByIdAndRemove', (done) => {
    assertNull(User.findByIdAndRemove(joe._id), done);
  });
});
