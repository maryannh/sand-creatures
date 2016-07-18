#!/usr/bin/python3
# -*- coding: utf-8 -*-


# from numpy.random import random
# from modules.helpers import _interpolate

from numpy import linspace
from modules.paths import get_displaced_single


SIZE = 2500
ONE = 1./SIZE

BACK = [1,1,1,1]
FRONT = [0,0,0,0.01]
RED = [0,0,0,0.01]

INUM = 5000
GRAINS = 20

EDGE = 0.1

CREATURE_NUM = 15

ORDERED = True

GAMMA = 1.5

NOISE = 0.0035


def make_creatures(sand):
  from modules.creature import Creature
  from numpy import array
  # from numpy.random import randint

  pnum = 4
  for i, y in enumerate(linspace(EDGE, 1.0-EDGE, CREATURE_NUM)):
    for j, x in enumerate(linspace(EDGE, 1.0-EDGE, CREATURE_NUM)):

      # pnum = randint(4,10)
      pnum = 4+i

      xy = array((x, y), 'float')
      size = 0.024
      creature = Creature(pnum, INUM, xy, size, ORDERED, get_displaced_single(NOISE))
      l1, l2 = creature.paths()
      sand.paint_strokes(l1, l2, GRAINS)

      # pnum += 1


def main():
  from sand import Sand
  from fn import Fn


  sand = Sand(SIZE)
  sand.set_rgba(FRONT)
  fn = Fn(prefix='./res/', postfix='.png')

  make_creatures(sand)
  # sand.set_bg_from_bw_array(bw)
  name = fn.name()
  sand.write_to_png(name, GAMMA)


if __name__ == '__main__':
  main()

