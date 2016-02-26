# coding: utf-8
from __future__ import absolute_import, division, print_function

from astropy.units import Quantity
from represent import ReprHelperMixin

from ..constants import (
    CONSTANT_OF_GRAVITATION, JUPITER_MASS, JUPITER_RADIUS_EQUATORIAL,
    JUPITER_RADIUS_POLAR, MARS_MASS, MARS_RADIUS_EQUATORIAL, MARS_RADIUS_POLAR,
    MERCURY_MASS, MERCURY_RADIUS_EQUATORIAL, MERCURY_RADIUS_POLAR,
    NEPTUNE_MASS, NEPTUNE_RADIUS_EQUATORIAL, NEPTUNE_RADIUS_POLAR, PLUTO_MASS,
    PLUTO_RADIUS_EQUATORIAL, PLUTO_RADIUS_POLAR, SATURN_MASS,
    SATURN_RADIUS_EQUATORIAL, SATURN_RADIUS_POLAR, URANUS_MASS,
    URANUS_RADIUS_EQUATORIAL, URANUS_RADIUS_POLAR, VENUS_MASS,
    VENUS_RADIUS_EQUATORIAL, VENUS_RADIUS_POLAR)
from ..util import read_only_property, verify_unit
from .ellipsoid import Ellipsoid, wgs84

__all__ = (
    'CelestialBody',
    'mercury',
    'venus',
    'earth',
    'mars',
    'jupiter',
    'saturn',
    'uranus',
    'neptune',
    'pluto',
)


class CelestialBody(ReprHelperMixin, object):
    """Celestial body.

    Parameters:
        name: Name of the celestial body.
        ellipsoid: Representative ellipsoid.
        mu: Standard gravitational parameter [m\ :sup:`3`\ ·s\ :sup:`-2`]
        naif_id: :term:`NAIF ID` for body.

    :type ellipsoid: :py:class:`~astrodynamics.bodies.ellipsoid.Ellipsoid`
    """
    def __init__(self, name, ellipsoid, mu, naif_id):
        self.name = name
        self._ellipsoid = ellipsoid
        self._mu = verify_unit(mu, 'm3 / s2')
        self._naif_id = naif_id

        self._mass = verify_unit(mu / CONSTANT_OF_GRAVITATION, 'kg')

    @classmethod
    def from_reference_ellipsoid(cls, name, ellipsoid, naif_id):
        """Construct from a
        :py:class:`~astrodynamics.bodies.ellipsoid.ReferenceEllipsoid`, which
        provides ``mu``.

        Parameters:
            name: Name of the celestial body.
            ellipsoid: Representative ellipsoid.
            naif_id: :term:`NAIF ID` for celestial body.

        :type ellipsoid: :py:class:`~astrodynamics.bodies.ellipsoid.ReferenceEllipsoid`
        """
        return cls(name=name, ellipsoid=ellipsoid, mu=ellipsoid.mu, naif_id=naif_id)

    ellipsoid = read_only_property('_ellipsoid')
    mu = read_only_property('_mu')
    mass = read_only_property('_mass')

    def _repr_helper_(self, r):
        r.keyword_from_attr('name')
        r.keyword_from_attr('ellipsoid')
        # View as Quantity to prevent full Constant repr.
        r.keyword_with_value('mu', self.mu.view(Quantity))
        r.keyword_from_attr('naif_id', '_naif_id')

    def __copy__(self):
        cls = self.__class__
        celestial_body = cls.__new__(cls)
        celestial_body.__dict__.update(self.__dict__)
        return celestial_body

G = CONSTANT_OF_GRAVITATION

mercury = CelestialBody(
    name='Mercury',
    ellipsoid=Ellipsoid(a=MERCURY_RADIUS_EQUATORIAL, b=MERCURY_RADIUS_POLAR),
    mu=G * MERCURY_MASS, naif_id=199)

venus = CelestialBody(
    name='Venus',
    ellipsoid=Ellipsoid(a=VENUS_RADIUS_EQUATORIAL, b=VENUS_RADIUS_POLAR),
    mu=G * VENUS_MASS, naif_id=299)

earth = CelestialBody.from_reference_ellipsoid(name='Earth', ellipsoid=wgs84, naif_id=399)

mars = CelestialBody(
    name='Mars',
    ellipsoid=Ellipsoid(a=MARS_RADIUS_EQUATORIAL, b=MARS_RADIUS_POLAR),
    mu=G * MARS_MASS, naif_id=499)

jupiter = CelestialBody(
    name='Jupiter',
    ellipsoid=Ellipsoid(a=JUPITER_RADIUS_EQUATORIAL, b=JUPITER_RADIUS_POLAR),
    mu=G * JUPITER_MASS, naif_id=599)

saturn = CelestialBody(
    name='Saturn',
    ellipsoid=Ellipsoid(a=SATURN_RADIUS_EQUATORIAL, b=SATURN_RADIUS_POLAR),
    mu=G * SATURN_MASS, naif_id=699)

uranus = CelestialBody(
    name='Uranus',
    ellipsoid=Ellipsoid(a=URANUS_RADIUS_EQUATORIAL, b=URANUS_RADIUS_POLAR),
    mu=G * URANUS_MASS, naif_id=799)

neptune = CelestialBody(
    name='Neptune',
    ellipsoid=Ellipsoid(a=NEPTUNE_RADIUS_EQUATORIAL, b=NEPTUNE_RADIUS_POLAR),
    mu=G * NEPTUNE_MASS, naif_id=899)

pluto = CelestialBody(
    name='Pluto',
    ellipsoid=Ellipsoid(a=PLUTO_RADIUS_EQUATORIAL, b=PLUTO_RADIUS_POLAR),
    mu=G * PLUTO_MASS, naif_id=999)
