#!/usr/bin/python3
# -*- coding: utf-8 -*-


SIZE = 1024
ONE = 1./SIZE

BACK = [1,1,1,1]
FRONT = [0,0,0,0.05]

PNUM = 5
INUM = 1000


def make_creatures(sand):
  from modules.creature import Creature

  creature = Creature(SIZE, PNUM, INUM)
  l1, l2 = creature.paths()
  sand.paint_strokes(l1, l2, INUM)


def main():
  from sand import Sand
  from fn import Fn


  sand = Sand(SIZE)
  sand.set_rgba(FRONT)
  fn = Fn(prefix='./res/', postfix='.png')

  make_creatures(sand)
  # sand.set_bg_from_bw_array(bw)
  name = fn.name()
  sand.write_to_png(name)


if __name__ == '__main__':
  main()

