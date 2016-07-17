
from numpy import zeros
from modules.helpers import random_points_in_circle

def _single(self):
  rnd = random_points_in_circle(
      self.pnum,
      self.xy[0],
      self.xy[1],
      self.size
      )

  return rnd, rnd

def _connected(self):
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
