import numpy as np
from mapf.Grid import *
from mapf.Astar import *
from gridgym.Visualiser import *
import time


def main():
	size = 8
	N = 3
	grid = np.random.rand(size, size) < 0.3

	env = Grid(grid)

	startend = get_positions(grid, 2*N)
	starts = [tuple(start) for start in startend[:N,:]]
	ends = [tuple(end) for end in startend[N:,:]]

	paths = astar_multi(env, starts, ends)

	print("starts: %s, ends: %s" % (starts, ends))
	print(paths)

	visualiser = Visualiser()

	if paths is None:
		visualiser.render(grid=grid, positions=np.array(starts), goals=np.array(ends))
	else:
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
			time.sleep(0.4)

	time.sleep(5)


def get_positions(grid, N):
	valid_i, valid_j = np.where(~grid)
	idxs = np.random.choice(len(valid_i), N, replace=False)
	pos_i = valid_i[idxs]
	pos_j = valid_j[idxs]
	return np.stack((pos_i, pos_j), axis=1)


if __name__ == '__main__':
	main()