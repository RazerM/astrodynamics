# coding: utf-8
from __future__ import absolute_import, division, print_function

from ..util import read_only_property, verify_unit


class CartesianState(object):
    def __init__(self, r, v, epoch, body):
        self._r = verify_unit(r, 'm')
        self._v = verify_unit(v, 'm / s')
        self._epoch = epoch
        self._body = body

    r = read_only_property('_r')
    v = read_only_property('_v')
    epoch = read_only_property('_epoch')
    body = read_only_property('_body')
