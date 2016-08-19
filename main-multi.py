#!/usr/bin/python3
# -*- coding: utf-8 -*-


BACK = [1,1,1,1]
FRONT = [0,0,0,0.001]

SIZE = 2000
ONE = 1./SIZE
EDGE = 0.1

GAMMA = 1.6

PATH_NUM = 10
PATH_INTERPOLATE_NUM = 100
PATH_SIZE = 0.35

TWIG_NUM = 10
TWIG_INTERPOLATE_NUM = 10000
TWIG_SIZE = 0.025

GRAINS = 13000


def make_creatures(sand):
  from modules.creature import MultiCreature
  from numpy import array

  for p in MultiCreature(
      array((0.5, 0.5), 'float'),
      PATH_SIZE,
      PATH_NUM,
      PATH_INTERPOLATE_NUM,
      TWIG_NUM,
      TWIG_INTERPOLATE_NUM,
      TWIG_SIZE
      ).paths(GRAINS):
    sand.paint_dots(p)


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

