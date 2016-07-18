#!/usr/bin/python3
# -*- coding: utf-8 -*-


from numpy import linspace
from modules.paths import get_displaced_single
from modules.paths import get_rnd_circ

BACK = [1,1,1,1]
FRONT = [0,0,0,0.0001]

SIZE = 1800
ONE = 1./SIZE

EDGE = 0.1

INUM = 60000
GRAINS = 60

CREATURE_NUM = 15
ORDERED = True

NOISE = 0.005

GAMMA = 1.5


def make_creatures(sand):
  from modules.creature import Creature
  from numpy import array
  # from numpy.random import randint

  pnum = 4
  for i, y in enumerate(linspace(EDGE, 1.0-EDGE, CREATURE_NUM)):
    for j, x in enumerate(linspace(EDGE, 1.0-EDGE, CREATURE_NUM)):

      # pnum = randint(4,10)
      pnum = 4+i
      # noise = 0.0030 + j*0.001

      xy = array((x, y), 'float')
      size = 0.024
      # creature = Creature(pnum, INUM, xy, size, get_displaced_single(NOISE), ORDERED)
      creature = Creature(pnum, INUM, xy, size, get_rnd_circ(NOISE), ORDERED)
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

