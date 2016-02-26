# coding: utf-8
from __future__ import absolute_import, division, print_function

from astrodynamics.io import TLE
from astrodynamics.propagation import SGP4
from astropy.time import Time

def test_sgp4():
    line1 = '1 25544U 98067A   08264.51782528 -.00002182  00000-0 -11606-4 0  2927'
    line2 = '2 25544  51.6416 247.4627 0006703 130.5360 325.0288 15.72125391563537'

    tle = TLE(line1, line2)
    sgp4 = SGP4(tle)
    state = sgp4.propagate_to(Time('2008:264', format='yday'))
    print(state.r, state.v)
    from numpy.linalg import norm
    print(norm(state.r), norm(state.v))
    assert False
