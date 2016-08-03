# -*- coding: utf-8 -*-

from modules.helpers import _rnd_interpolate
from modules.helpers import _interpolate


class Creature(object):
  def __init__(
      self,
      pnum,
      inum,
      xy,
      size,
      path_function,
      ordered = False,
      linear = False
      ):
    self.i = 0
    self.pnum = pnum
    self.inum = inum
    self.xy = xy
    self.size = size
    self.path_function = path_function

    self.linear = linear
    self.ordered = ordered

    xy1, xy2 = path_function(self)
    self.xy1 = xy1
    self.xy2 = xy2

  def paths(self):
    if not self.linear:
      l1 = _rnd_interpolate(self.xy1, self.inum, ordered=self.ordered)
      l2 = _rnd_interpolate(self.xy2, self.inum, ordered=self.ordered)
    else:
      l1 = _interpolate(self.xy1, self.inum)
      l2 = _interpolate(self.xy2, self.inum)
    return l1, l2

class MultiCreature(object):
  def __init__(
      self,
      pnum,
      inum,
      steps,
      xy,
      size,
      path_function
      ):
    self.i = 0
    self.pnum = pnum
    self.inum = inum
    self.xy = xy
    self.size = size
    self.path_function = path_function
    self.steps = steps

    _paths =  path_function(self)
    self._paths = []

    for p in _paths:
      self._paths.append(_rnd_interpolate(p, steps, ordered=True))

  def paths(self):
    from numpy import row_stack
    for i in range(self.steps):
      xy = row_stack([p[i,:] for p in self._paths])
      yield _rnd_interpolate(xy, self.inum, ordered=True)

