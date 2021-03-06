const DriversController = require('../controllers/drivers.controller');

module.exports = (app) => {
  app.get('/api', DriversController.ready);

  app.get('/api/drivers', DriversController.index);
  app.post('/api/drivers', DriversController.create);
  app.put('/api/drivers/:id', DriversController.edit);
  app.delete('/api/drivers/:id', DriversController.delete);
};
