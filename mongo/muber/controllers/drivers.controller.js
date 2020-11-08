const Driver = require('../models/drivers');

module.exports = {
  ready: (req, res) => {
    res.sendStatus(200);
  },

  index: (req, res, next) => {
    const {
      query: { lng, lat },
    } = req;

    Driver.aggregate([
      {
        $geoNear: {
          near: {
            type: 'Point',
            coordinates: [parseFloat(lng), parseFloat(lat)],
          },
          maxDistance: 200000,
          spherical: true,
          distanceField: 'dist.calculated',
        },
      },
    ])
      .then((drivers) => res.send(drivers))
      .catch(next);
  },

  create: (req, res, next) => {
    const { body } = req;

    Driver.create(body)
      .then((driver) => res.send(driver))
      .catch(next);
  },

  edit: (req, res, next) => {
    const {
      body,
      params: { id },
    } = req;

    Driver.findByIdAndUpdate(id, body)
      .then(() => Driver.findById(id))
      .then((driver) => res.status(200).send(driver))
      .catch(next);
  },

  delete: (req, res, next) => {
    const {
      params: { id },
    } = req;

    Driver.findByIdAndDelete(id)
      .then((driver) => res.status(200).send(driver))
      .catch(next);
  },
};
