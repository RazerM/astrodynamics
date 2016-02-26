# coding: utf-8
from __future__ import absolute_import, division, print_function

from ..util import read_only_property


class TLE(object):
    def __init__(self, line1, line2):
        self._line1 = line1
        self._line2 = line2

    line1 = read_only_property('_line1')
    line2 = read_only_property('_line2')
