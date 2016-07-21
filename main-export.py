#!/usr/bin/python3
# -*- coding: utf-8 -*-


from numpy import linspace
from modules.paths import get_displaced_single
# from modules.paths import get_rnd_circ

BACK = [1,1,1,1]
FRONT = [0,0,0,1.0]

SIZE = 1800
ONE = 1./SIZE

EDGE = 0.1

INUM = 200

CREATURE_NUM = 12
ORDERED = True

NOISE = 0.005

GAMMA = 1.5


def make_creatures(sand):
  from modules.creature import Creature
  from numpy import array
  from numpy import row_stack
  from numpy import arange
  # from numpy.random import randint

  lines = []
  vertices = []

  vnum = 0

  pnum = 4
  for i, y in enumerate(linspace(EDGE, 1.0-EDGE, CREATURE_NUM)):
    for j, x in enumerate(linspace(EDGE, 1.0-EDGE, CREATURE_NUM)):

      # pnum = randint(4,10)
      pnum = 4+i
      # noise = 0.0030 + j*0.001

      xy = array((x, y), 'float')
      size = 0.025
      creature = Creature(
          pnum,
          INUM,
          xy,
          size,
          get_displaced_single(NOISE),
          linear=True
          )
      l1, l2 = creature.paths()

      vertices.append(l1)
      lines.append(arange(INUM).astype('int')+vnum)
      vnum += INUM

      vertices.append(l2)
      lines.append(arange(INUM).astype('int')+vnum)
      vnum += INUM

      sand.paint_dots(l1)
      sand.paint_dots(l2)

      print(len(l1))

  return row_stack(vertices), lines


def main():
  from sand import Sand
  from fn import Fn

  from iutils.ioOBJ import export_2d as export


  sand = Sand(SIZE)
  sand.set_rgba(FRONT)
  fn = Fn(prefix='./res/')

  vertices, lines = make_creatures(sand)

  name = fn.name()
  sand.write_to_png(name + '.png', GAMMA)
  export('scribbles', name + '.2obj', verts=vertices, lines=lines)



if __name__ == '__main__':
  main()

