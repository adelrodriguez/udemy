const assert = require('assert');
const request = require('supertest');
const app = require('../app');

describe('The express app', () => {
  it('GET /api', (done) => {
    request(app)
      .get('/api')
      .end((err, response) => {
        assert(response.status === 200);
        done();
      });
  });
});
