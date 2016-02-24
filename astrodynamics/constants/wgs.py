# coding: utf-8
from __future__ import absolute_import, division, print_function

from astropy import units as u  # flake8: noqa

# Absolute import used here so file can be exec'd
# standalone by documentation helper script.
from astrodynamics.constants import Constant  # flake8: noqa

__all__ = (
    'WGS84_EQUATORIAL_RADIUS',
    'WGS84_FLATTENING',
    'WGS84_MU',
    'WGS84_ANGULAR_VELOCITY',
    'WGS72_EQUATORIAL_RADIUS',
    'WGS72_FLATTENING',
    'WGS72_MU',
    'WGS72_ANGULAR_VELOCITY',
)

WGS84_EQUATORIAL_RADIUS = Constant(
    name='WGS84 semi-major axis',
    value=6378137,
    unit='m',
    uncertainty=0,
    reference='World Geodetic System 1984')

WGS84_FLATTENING = Constant(
    name='WGS84 Earth flattening factor',
    value=1 / 298.257223563,
    unit='',
    uncertainty=0,
    reference='World Geodetic System 1984')

WGS84_MU = Constant(
    name='WGS84 geocentric gravitational constant',
    value=3986004.418e8,
    unit='m3 / s2',
    uncertainty=0.008,
    reference='World Geodetic System 1984')

WGS84_ANGULAR_VELOCITY = Constant(
    name='WGS84 nominal earth mean angular velocity',
    value=7292115.0e-11,
    unit='rad / s',
    uncertainty=0,
    reference='World Geodetic System 1984')

WGS72_EQUATORIAL_RADIUS = Constant(
    name='WGS72 semi-major axis',
    value=6378135,
    unit='m',
    uncertainty=5,
    reference='World Geodetic System 1972')

WGS72_FLATTENING = Constant(
    name='WGS72 Earth flattening factor',
    value=1 / 298.26,
    unit='',
    uncertainty=0.6e-7,
    reference='World Geodetic System 1972')

WGS72_MU = Constant(
    name='WGS72 geocentric gravitational constant',
    value=398600.5,
    unit='km3 / s2',
    uncertainty=0.4,
    reference='World Geodetic System 1972')

WGS72_ANGULAR_VELOCITY = Constant(
    name='WGS72 nominal earth mean angular velocity',
    value=0.7292115147e-4,
    unit='rad / s',
    uncertainty=0.1e-13,
    reference='World Geodetic System 1972')
