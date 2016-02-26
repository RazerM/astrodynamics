# coding: utf-8
from __future__ import absolute_import, division, print_function

from copy import copy

import astropy.units as u
from sgp4.io import twoline2rv
from sgp4.propagation import sgp4

from ..bodies import earth, wgs72
from ..state import CartesianState


class SGP4(object):
    """Adapter class for sgp4 module, which uses the C++ API"""
    def __init__(self, tle, gravity_model=wgs72):
        if gravity_model._sgp4_constants is None:
            raise TypeError(
                'gravity_model._sgp4_constants must be an sgp4.earth_gravity.'
                'EarthGravity instance for use with the sgp4 module.')

        self.tle = tle
        self.gravity_model = gravity_model
        self._satellite = twoline2rv(
            tle.line1, tle.line2, gravity_model._sgp4_constants)

    def propagate_to(self, time):
        minutes = (time.jd - self._satellite.jdsatepoch) * 1440
        r, v = sgp4(self._satellite, minutes)

        if self._satellite.error:
            raise ValueError(self._satellite.error_message)

        body = earth

        # If we're using a different ellipsoid than `earth`, create a
        # new CelestialBody with our ellipsoid.
        if body.ellipsoid is not earth.ellipsoid:
            body = copy(earth)
            body._ellipsoid = self.gravity_model

        return CartesianState(r * u.km, v * u.km / u.s, epoch=time, body=body)
