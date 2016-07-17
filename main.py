#!/usr/bin/python3
# -*- coding: utf-8 -*-


SIZE = 2000
ONE = 1./SIZE

BACK = [1,1,1,1]
FRONT = [0,0,0,0.01]

INUM = 30000
GRAINS = 100

EDGE = 0.3

CREATURE_NUM = 2

ORDERED = True

GAMMA = 1.5


def make_creatures(sand):
  from modules.creature import Creature
  from numpy import array
  from numpy.random import randint
  from numpy import linspace

  for x in linspace(EDGE, 1.0-EDGE, CREATURE_NUM):
    for y in linspace(EDGE, 1.0-EDGE, CREATURE_NUM):

      pnum = randint(4,10)

      xy = array((x, y), 'float')
      size = 0.035*5
      creature = Creature(pnum, INUM, xy, size, ordered=ORDERED)
      l1, l2 = creature.paths()
      sand.paint_strokes(l1, l2, GRAINS)


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

