import numpy as np
from mapf.Grid import *
from mapf.CBS import *
from gridgym.Visualiser import *
import time


def main():

  grid = get_grid()
  env = Grid(grid)

  starts = get_starts()
  ends = get_goals()

  paths = cbs(env, starts, ends)

  visualiser = Visualiser()

  if paths is None:
    visualiser.render(grid=grid, positions=np.array(starts), goals=np.array(ends))
  else:
    for i in range(len(paths)):
      if paths[i] is None:
        paths[i] = [starts[i]]
    maxlength = max([len(path) for path in paths])
    for i in range(maxlength):
      positions = np.zeros((len(paths),2)).astype(int)
      for j in range(len(paths)):
        if i < len(paths[j]):
          positions[j,:] = paths[j][i]
        else:
          positions[j,:] = paths[j][-1]
      goals = np.array(ends)
      visualiser.render(grid=grid, positions=positions, goals=goals)
      time.sleep(0.3)

  import pdb; pdb.set_trace()


def get_goals():
	return np.array([[14, 16],
       [10, 22],
       [ 5, 12],
       [ 0,  6],
       [22,  1],
       [ 7, 19],
       [ 2, 18],
       [ 9, 22],
       [19,  1],
       [18,  6],
       [21, 20],
       [ 4, 18]])


def get_starts():
	return np.array([[18, 10],
       [18,  3],
       [14, 22],
       [14,  8],
       [ 8,  3],
       [ 0, 14],
       [13,  6],
       [13, 11],
       [21,  6],
       [20, 22],
       [ 7,  6],
       [20,  9]])


def get_grid():
	return np.array([[False, False, False, False, False, False, False, False, False,
        False, False,  True, False, False, False, False, False, False,
        False, False, False, False, False,  True],
       [False, False, False, False, False, False, False, False,  True,
        False, False, False, False, False,  True, False, False,  True,
        False, False, False,  True,  True, False],
       [ True, False,  True, False, False,  True, False, False, False,
        False, False, False,  True, False, False, False,  True,  True,
        False,  True, False, False,  True, False],
       [False, False, False, False, False, False, False,  True, False,
        False,  True, False,  True,  True,  True,  True,  True,  True,
        False, False,  True, False, False, False],
       [False, False, False, False,  True, False, False, False, False,
         True, False, False,  True, False, False,  True, False, False,
        False, False, False, False,  True, False],
       [ True, False, False,  True, False, False, False, False, False,
        False, False, False, False, False, False,  True,  True,  True,
         True, False, False, False, False, False],
       [False, False, False, False,  True, False,  True,  True, False,
        False, False, False,  True, False, False, False, False,  True,
         True, False,  True, False,  True,  True],
       [False, False, False, False, False, False, False,  True, False,
        False, False, False,  True, False, False, False, False, False,
        False, False, False, False, False,  True],
       [False, False,  True, False, False, False,  True, False, False,
        False, False, False,  True, False, False,  True, False, False,
        False, False, False, False, False, False],
       [ True, False, False,  True, False,  True,  True, False, False,
        False, False,  True, False, False,  True,  True, False,  True,
        False,  True,  True, False, False,  True],
       [False,  True, False, False, False, False,  True, False, False,
         True, False, False, False, False, False,  True, False, False,
        False, False, False, False, False, False],
       [ True, False, False,  True, False, False, False,  True, False,
        False,  True,  True, False, False, False, False, False, False,
        False, False, False, False, False, False],
       [False, False, False, False, False,  True, False, False, False,
        False,  True, False, False,  True, False, False,  True,  True,
        False, False, False, False, False,  True],
       [ True,  True, False, False, False,  True, False,  True,  True,
         True, False, False, False,  True,  True, False,  True, False,
        False, False, False, False, False,  True],
       [False,  True, False, False,  True,  True,  True, False, False,
        False, False,  True,  True, False, False, False, False,  True,
        False,  True,  True,  True, False, False],
       [False, False,  True,  True, False, False, False,  True, False,
        False, False, False, False,  True, False, False,  True, False,
        False, False, False, False, False, False],
       [False, False, False, False, False, False, False, False,  True,
         True,  True, False, False, False,  True, False, False, False,
        False, False, False, False, False, False],
       [ True, False, False, False,  True,  True, False, False, False,
        False, False, False, False, False,  True,  True, False, False,
         True, False, False,  True, False, False],
       [False, False, False, False, False, False, False, False, False,
         True, False, False,  True, False, False, False, False, False,
        False, False, False, False,  True, False],
       [False, False,  True, False, False, False, False, False,  True,
         True, False, False, False,  True, False,  True, False, False,
        False, False, False, False,  True,  True],
       [ True, False,  True, False, False, False, False,  True,  True,
        False, False, False, False,  True, False, False, False, False,
         True, False, False, False, False, False],
       [ True, False, False, False, False, False, False, False, False,
        False, False, False, False, False,  True,  True, False, False,
        False, False, False, False, False, False],
       [False, False,  True, False,  True,  True, False,  True,  True,
        False,  True,  True, False, False, False,  True,  True, False,
         True,  True,  True, False,  True, False],
       [ True, False, False, False, False,  True, False,  True, False,
        False, False, False, False, False,  True,  True, False, False,
        False, False, False, False, False, False]])


if __name__ == '__main__':
	main()