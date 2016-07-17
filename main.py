#!/usr/bin/python3
# -*- coding: utf-8 -*-


SIZE = 1024
ONE = 1./SIZE

BACK = [1,1,1,1]
FRONT = [0,0,0,0.05]

INUM = 5

def make_creatures(sand):
  from creature import Creature

  creature = Creature(SIZE, INUM)

  # dots = creature.step()


def main():
  from sand import Sand
  from fn import Fn


  sand = Sand(SIZE)
  sand.set_rgba(FRONT)
  fn = Fn(prefix='./res/', postfix='.png')

  make_creatures(sand)

  # try:
  #   while True:
  #     t0 = time()
  #     itt = dunes.steps(LEAP)
  #     print(itt, time()-t0)
  #     dunes.get_normalized_sand_limit(bw, 10)
  #     # bw *= 0.8
  #     # sand.set_bg_from_bw_array(bw)
  #     # dunes.get_shadow(shadow)
  #     # rgb = dstack((bw,bw,shadow))
  #     # sand.set_bg_from_rgb_array(rgb)
  #     sand.set_bg_from_bw_array(bw)
  #     name = fn.name()
  #     sand.write_to_png(name)
  # except KeyboardInterrupt:
  #   pass


if __name__ == '__main__':
  main()

