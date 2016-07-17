# -*- coding: utf-8 -*-

from numpy import pi
from numpy import column_stack
from numpy import sin
from numpy import cos
from numpy import reshape
from numpy import zeros
from numpy.random import random

from .helpers import _rnd_interpolate

ORDERED = True


TWOPI = pi*2
HPI = pi*0.5

class Creature(object):
  def __init__(
      self,
      inum
      ):
    self.i = 0
    self.inum = inum

    # self.interpolated_path = _rnd_interpolate(path, inum, ordered=ORDERED)

    rnd = random((2*inum-1, 2))

    self.xy1 = rnd[:inum,:]
    self.xy2 = zeros((inum,2), 'float')
    self.xy2[0,:] = rnd[0,:]
    self.xy2[-1,:] = rnd[inum-1,:]
    self.xy2[1:-1,:] = rnd[inum:-1,:]

    print(self.xy1)
    print(self.xy2)

  def __iter__(self):
      return self

  # def __next__(self):
  #
  #   if self.i<
  #
  #
  #     g = next(self.guide)
  #   except Exception:
  #     raise StopIteration
  #
  #   pnum = self.pnum
  #
  #   r = 1.0-2.0*random(pnum)
  #   self.noise[:] += r*self.scale
  #
  #   a = random(pnum)*TWOPI
  #   rnd = column_stack((cos(a), sin(a)))
  #
  #   self.path += rnd * reshape(self.noise, (self.pnum,1))
  #   self.interpolated_path = _rnd_interpolate(self.path, self.inum, ordered=ORDERED)
  #
  #   self.i+=1
  #   return g + self.interpolated_path
  #
