#!/usr/bin/python3
# -*- coding: utf-8 -*-


from numpy import linspace
from modules.paths import get_displaced_single
# from modules.paths import get_rnd_circ
# from modules.paths import get_connected

BACK = [1,1,1,1]
FRONT = [0,0,0,0.0001]

SIZE = 4000
ONE = 1./SIZE

EDGE = 0.1

INUM = 20000
GRAINS = 500

CREATURE_NUM = 13
ORDERED = True

NOISE = 0.005

GAMMA = 1.6


def make_creatures(sand):
  from modules.creature import Creature
  from numpy import array
  from numpy.random import randint
  from modules.helpers import get_colors
  from numpy.random import random
  from numpy import sqrt

  # colors = get_colors('../colors/shimmering.gif')
  # colors = get_colors('../colors/tumblr_nkpio2Dl4H1rlz4gso2_1280_1000.jpg')
  # colors = get_colors('../colors/ir.jpg')
  colors = get_colors('../colors/black_green.gif')
  nc = len(colors)

  w = 0
  # for i, y in enumerate(linspace(EDGE, 1.0-EDGE, CREATURE_NUM)):
  #   for j, x in enumerate(linspace(EDGE, 1.0-EDGE, CREATURE_NUM)):

  for i in range(400):
    print(i)

    pnum = randint(4,8)
    # pnum = 4+j
    # pnum = 5
    # noise = 0.0030 + j*0.001

    xy = array((EDGE + random()*(1.0-2.0*EDGE),EDGE + random()*(1.0-2.0*EDGE)), 'float')
    size = 0.03
    creature = Creature(pnum, INUM, xy, size, get_displaced_single(NOISE), ORDERED)
    # creature = Creature(pnum, INUM, xy, size, get_rnd_circ(NOISE), ORDERED)
    # creature = Creature(pnum, INUM, xy, size, get_connected(), ORDERED)
    l1, l2 = creature.paths()

    w += 1
    rgba = colors[w%nc] + [0.0005]
    sand.set_rgba(rgba)
    sand.paint_strokes(l1, l2, GRAINS)

      # pnum += 1


def main():
  from sand import Sand
  from fn import Fn


  sand = Sand(SIZE)
  sand.set_bg(BACK)
  sand.set_rgba(FRONT)
  fn = Fn(prefix='./res/', postfix='.png')

  make_creatures(sand)
  # sand.set_bg(bw)
  name = fn.name()
  sand.write_to_png(name, GAMMA)


if __name__ == '__main__':
  main()

