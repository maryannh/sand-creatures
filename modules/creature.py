# -*- coding: utf-8 -*-

from numpy import zeros
from numpy.random import random

from modules.helpers import _rnd_interpolate
from modules.helpers import _interpolate

from modules.helpers import random_points_in_circle

ORDERED = True


class Creature(object):
  def __init__(
      self,
      pnum,
      inum,
      xy,
      size,
      ordered
      ):
    self.i = 0
    self.pnum = pnum
    self.inum = inum
    self.xy = xy
    self.size = size

    self.ordered = ordered

    self._connected()
    # self._unconnected()


  def _connected(self):
    pnum = self.pnum
    # rnd = self.xy + (1.0-2.0*random((2*pnum-1, 2)))*self.size
    rnd = random_points_in_circle(
        2*pnum-1,
        self.xy[0],
        self.xy[1],
        self.size
        )
    self.xy1 = rnd[:pnum,:]
    self.xy2 = zeros((pnum,2), 'float')
    self.xy2[0,:] = rnd[0,:]
    self.xy2[-1,:] = rnd[pnum-1,:]
    self.xy2[1:-1,:] = rnd[pnum:-1,:]

  def _unconnected(self):
    pnum = self.pnum
    rnd = self.xy + (1.0-2.0*random((2*pnum, 2)))*self.size
    self.xy1 = rnd[:pnum,:]
    self.xy2 = rnd[pnum:,:]

  def __iter__(self):
      return self

  def paths(self):
    l1 = _rnd_interpolate(self.xy1, self.inum, ordered=self.ordered)
    l2 = _rnd_interpolate(self.xy2, self.inum, ordered=self.ordered)
    # l1 = _interpolate(self.xy1, self.inum)
    # l2 = _interpolate(self.xy2, self.inum)
    return l1, l2

