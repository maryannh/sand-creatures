#!/usr/bin/python3
# -*- coding: utf-8 -*-


from numpy import linspace
from modules.paths import get_displaced_multi

BACK = [1,1,1,1]
FRONT = [0,0,0,0.001]

SIZE = 1800
ONE = 1./SIZE

EDGE = 0.1

INUM = 200
STEPS = 10000

CREATURE_NUM = 10

NOISE = 0.03

GAMMA = 1.5


def make_creatures(sand):
  from modules.creature import MultiCreature
  from numpy import array

  pnum = 4
  for i, y in enumerate(linspace(EDGE, 1.0-EDGE, CREATURE_NUM)):
    for j, x in enumerate(linspace(EDGE, 1.0-EDGE, CREATURE_NUM)):
      print(i,j)

      pnum = 4
      xy = array((x, y), 'float')
      size = (1.0-2*EDGE)/CREATURE_NUM*0.1
      creature = MultiCreature(
          pnum,
          INUM,
          STEPS,
          xy,
          size,
          get_displaced_multi(NOISE, 10)
          )
      for l1 in creature.paths():
        sand.paint_dots(l1)


def main():
  from sand import Sand
  from fn import Fn


  sand = Sand(SIZE)
  sand.set_rgba(FRONT)
  fn = Fn(prefix='./res/', postfix='.png')

  make_creatures(sand)
  name = fn.name()
  sand.write_to_png(name, GAMMA)


if __name__ == '__main__':
  main()

