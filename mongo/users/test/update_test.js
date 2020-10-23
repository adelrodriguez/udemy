const assert = require('assert');
const User = require('../src/models/user.model');

describe('Updating records', () => {
  let joe;

  beforeEach((done) => {
    joe = new User({ name: 'Joe', likes: 0 });

    joe.save().then(() => {
      done();
    });
  });

  function assertName(operation, done) {
    operation
      .then(() => User.find())
      .then((users) => {
        assert(users.length === 1);
        assert(users[0].name === 'Jimmy');
        done();
      });
  }

  it('model instance set and save', (done) => {
    joe.set('name', 'Jimmy');

    assertName(joe.save(), done);
  });

  it('model instance can update', (done) => {
    assertName(joe.update({ name: 'Jimmy' }), done);
  });

  it('class method update', (done) => {
    assertName(User.update({ name: 'Joe' }, { name: 'Jimmy' }), done);
  });

  it('class method findOneAndUpdate', (done) => {
    assertName(User.findOneAndUpdate({ name: 'Joe' }, { name: 'Jimmy' }), done);
  });

  it('class method findByIdAndUpdate', (done) => {
    assertName(User.findByIdAndUpdate(joe._id, { name: 'Jimmy' }), done);
  });

  it('user has their likes incremented by 1', (done) => {
    User.update({ name: 'Joe' }, { $inc: { likes: 1 } })
      .then(() => User.findOne({ name: 'Joe' }))
      .then((user) => {
        assert(user.likes === 1);
        done();
      });
  });
});
