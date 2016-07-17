# -*- coding: utf-8 -*-

from numpy import zeros
from numpy.random import random

from .helpers import _rnd_interpolate

ORDERED = True


class Creature(object):
  def __init__(
      self,
      size,
      pnum,
      inum
      ):
    self.i = 0
    self.size = size
    self.pnum = pnum
    self.inum = inum

    rnd = 0.1 + random((2*pnum-1, 2))*0.8

    self.xy1 = rnd[:pnum,:]
    self.xy2 = zeros((pnum,2), 'float')
    self.xy2[0,:] = rnd[0,:]
    self.xy2[-1,:] = rnd[pnum-1,:]
    self.xy2[1:-1,:] = rnd[pnum:-1,:]


  def __iter__(self):
      return self

  def paths(self):
    l1 = _rnd_interpolate(self.xy1, self.inum, ordered=True)
    l2 = _rnd_interpolate(self.xy2, self.inum, ordered=True)
    return l1, l2

