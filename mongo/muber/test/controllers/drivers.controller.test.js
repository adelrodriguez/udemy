const assert = require('assert');
const request = require('supertest');
const mongoose = require('mongoose');
const app = require('../../app');

const Driver = mongoose.model('driver');

describe('Drivers controller', () => {
  it('POST /api/drivers', (done) => {
    Driver.count().then((count) => {
      request(app)
        .post('/api/drivers')
        .send({ email: 'test@test.com' })
        .end(() => {
          Driver.count().then((newCount) => {
            assert(count + 1 === newCount);
            done();
          });
        });
    });
  });

  it('PUT /api/drivers/:id', (done) => {
    Driver.create({ email: 'jim@test.com' }).then((driver) => {
      request(app)
        .put(`/api/drivers/${driver.id}`)
        .send({ driving: true })
        .end(() => {
          Driver.findById(driver.id).then((updatedDriver) => {
            assert(updatedDriver.driving === true);
            done();
          });
        });
    });
  });

  it('DELETE /api/drivers/:id', (done) => {
    Driver.create({ email: 'jim@test.com' }).then((driver) => {
      Driver.count().then((count) => {
        request(app)
          .delete(`/api/drivers/${driver.id}`)
          .end(() => {
            Driver.count().then((newCount) => {
              assert(count - 1 === newCount);
              done();
            });
          });
      });
    });
  });

  it('GET /api/drivers', (done) => {
    const seattleDriver = new Driver({
      email: 'seattle@test.com',
      geometry: { type: 'Point', coordinates: [-122.475902, 47.6147628] },
    });

    const miamiDriver = new Driver({
      email: 'miami@test.com',
      geometry: { type: 'Point', coordinates: [-80.253, 25.791]}
    });

    Promise.all([seattleDriver.save(), miamiDriver.save()]).then(() => {
      request(app)
        .get('/api/drivers?lng=-80&lat=25')
        .end((err, response) => {
          assert(response.body.length === 1);
          assert(response.body[0].email === 'miami@test.com')
          done();
        });
    })
  });
});
