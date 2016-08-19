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
      xy,
      path_size,
      path_num,
      path_interpolate_num,
      twig_num,
      twig_interpolate_num,
      twig_size
      ):
    from modules.helpers import random_points_in_circle
    from numpy import dstack
    self.i = 0

    self.xy = xy
    self.psize = path_size
    self.pnum = path_num
    self.pinum = path_interpolate_num

    self.tnum = twig_num
    self.tinum = twig_interpolate_num
    self.tsize = twig_size

    path = random_points_in_circle(
        self.pnum,
        self.xy[0],
        self.xy[1],
        self.psize
        )

    interpolated_twigs = []
    for x in _rnd_interpolate(path, self.pinum, ordered=True):
      twig = random_points_in_circle(
          self.tnum,
          x[0],
          x[1],
          self.tsize
          )
      interpolated_twigs.append(_rnd_interpolate(twig, self.tinum, ordered=True))

    self.itwigs = dstack(interpolated_twigs)

  def paths(self, grains, ordered=False):
    from numpy import transpose
    for r in range(self.tinum):
      row = self.itwigs[r,:,:]
      yield _rnd_interpolate(transpose(row), grains, ordered=ordered)

