#!/usr/bin/python3
# -*- coding: utf-8 -*-


from numpy import linspace
from modules.paths import get_displaced_single
# from modules.paths import get_rnd_circ

BACK = [1,1,1,1]
FRONT = [0,0,0,0.0001]

SIZE = 4000
ONE = 1./SIZE

EDGE = 0.1

INUM = 20000
GRAINS = 150

CREATURE_NUM = 15
ORDERED = True

NOISE = 0.005

GAMMA = 1.5


def make_creatures(sand):
  from modules.creature import Creature
  from numpy import array
  from numpy.random import randint
  from modules.helpers import get_colors

  # colors = get_colors('../colors/shimmering.gif')
  # colors = get_colors('../colors/tumblr_nkpio2Dl4H1rlz4gso2_1280_1000.jpg')
  colors = get_colors('../colors/ray-1.jpeg')
  nc = len(colors)

  w = 0
  pnum = 4
  for i, y in enumerate(linspace(EDGE, 1.0-EDGE, CREATURE_NUM)):
    for j, x in enumerate(linspace(EDGE, 1.0-EDGE, CREATURE_NUM)):

      # pnum = randint(4,10)
      pnum = 4+j
      # pnum = 5
      noise = 0.0030 + j*0.001

      xy = array((x, y), 'float')
      size = 0.024
      creature = Creature(pnum, INUM, xy, size, get_displaced_single(noise), ORDERED)
      # creature = Creature(pnum, INUM, xy, size, get_rnd_circ(), ORDERED)
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
  sand.set_rgba(FRONT)
  fn = Fn(prefix='./res/', postfix='.png')

  make_creatures(sand)
  # sand.set_bg_from_bw_array(bw)
  name = fn.name()
  sand.write_to_png(name, GAMMA)


if __name__ == '__main__':
  main()

