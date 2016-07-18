
from numpy import zeros
from numpy.random import random
from numpy import column_stack
from numpy import cos
from numpy import sin
from numpy import pi
from modules.helpers import random_points_in_circle

TWOPI = 2*pi

def get_single():
  def f(self):
    rnd = random_points_in_circle(
        self.pnum,
        self.xy[0],
        self.xy[1],
        self.size
        )
    return rnd, rnd
  return f


def get_displaced_single(noise):
  def f(self):
    rnd = random_points_in_circle(
        self.pnum,
        self.xy[0],
        self.xy[1],
        self.size
        )

    a = random(self.pnum)*TWOPI
    rad = random(size=(self.pnum,1))
    disp = column_stack((cos(a), sin(a)))*noise*rad
    return rnd, rnd+disp
  return f

def get_connected():
  def f(self):
    rnd = random_points_in_circle(
        2*self.pnum-1,
        self.xy[0],
        self.xy[1],
        self.size
        )
    xy1 = rnd[:self.pnum,:]
    xy2 = zeros((self.pnum,2), 'float')
    xy2[0,:] = rnd[0,:]
    xy2[-1,:] = rnd[self.pnum-1,:]
    xy2[1:-1,:] = rnd[self.pnum:-1,:]
    return xy1, xy2
  return f
