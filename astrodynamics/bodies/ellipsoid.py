# coding: utf-8
from __future__ import absolute_import, division, print_function

from astropy.units import Quantity
from represent import ReprHelperMixin

from ..constants import (
    WGS72_ANGULAR_VELOCITY, WGS72_EQUATORIAL_RADIUS, WGS72_FLATTENING,
    WGS72_MU, WGS84_ANGULAR_VELOCITY, WGS84_EQUATORIAL_RADIUS,
    WGS84_FLATTENING, WGS84_MU)
from ..util import read_only_property, verify_unit

__all__ = (
    'Ellipsoid',
    'ReferenceEllipsoid',
    'wgs84',
)


class Ellipsoid(ReprHelperMixin, object):
    """Ellipsoid

    Parameters:
        a: Semi-major axis (equatorial radius) [m]
        b: Semi-minor axis (polar radius) [m]
        f: Flattening [-]

    Either ``b`` or ``f`` must be specified: the other will be calculated.
    """
    def __init__(self, a, b=None, f=None):
        if (b is None and f is None) or (b and f):
            raise TypeError('Either b or f must be specified, but not both.')

        self._a = verify_unit(a, 'm')

        if b is None:
            self._b = verify_unit(a * (1 - f), 'm')
            self._f = verify_unit(f, '')

        if f is None:
            self._b = verify_unit(b, 'm')
            self._f = verify_unit(1 - (b / a), '')

    a = read_only_property('_a', 'Semi-major axis')
    b = read_only_property('_b', 'Semi-minor axis')
    f = read_only_property('_f', 'Flattening')

    def _repr_helper_(self, r):
        # View as Quantity to prevent full Constant repr.
        r.keyword_with_value('a', self.a.view(Quantity))
        r.keyword_with_value('f', self.f.view(Quantity))


class ReferenceEllipsoid(Ellipsoid):
    """ReferenceEllipsoid

    Parameters:
        a: Semi-major axis (equatorial radius) [m]
        f: Flattening [-]
        mu: Standard gravitational parameter [m\ :sup:`3`\ ·s\ :sup:`-2`]
        spin: Spin rate [rad/s]
    """
    def __init__(self, a, f, mu, spin):
        super(ReferenceEllipsoid, self).__init__(a=a, f=f)
        self._mu = verify_unit(mu, 'm3 / s2')
        self._spin = verify_unit(spin, 'rad / s')

    mu = read_only_property('_mu', 'Standard gravitational parameter')
    spin = read_only_property('_spin', 'Angular velocity')

    def _repr_helper_(self, r):
        super(ReferenceEllipsoid, self)._repr_helper_(r)
        # View as Quantity to prevent full Constant repr.
        r.keyword_with_value('mu', self.mu.view(Quantity))
        r.keyword_with_value('spin', self.spin.view(Quantity))

wgs84 = ReferenceEllipsoid(
    a=WGS84_EQUATORIAL_RADIUS,
    f=WGS84_FLATTENING,
    mu=WGS84_MU,
    spin=WGS84_ANGULAR_VELOCITY)

wgs72 = ReferenceEllipsoid(
    a=WGS72_EQUATORIAL_RADIUS,
    f=WGS72_FLATTENING,
    mu=WGS72_MU,
    spin=WGS72_ANGULAR_VELOCITY)
