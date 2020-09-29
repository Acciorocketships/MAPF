import numpy as np
from mapf.Grid import *
from mapf.Assignment import *
from gridgym.Visualiser import *
import time


def main():
	size = 28
	N = 5
	grid = np.random.rand(size, size) < 0.3

	env = Grid(grid)

	startend = get_positions(grid, 2*N)
	starts = np.array([tuple(start) for start in startend[:N,:]])
	goals = np.array([tuple(goal) for goal in startend[N:,:]])

	visualiser = Visualiser()

	costmat = Assignment.compute_matrix(env, starts, goals)
	print('cost matrix:')
	print(costmat)
	assignment = Assignment.hungarian(costmat)
	print('assignment permutation:')
	print(assignment)

	positions = starts.copy()
	while not np.all(positions==goals):
		action = Assignment.action(env, positions, goals, assignment)
		positions += action.astype(int)
		visualiser.render(grid=grid, positions=positions, goals=goals)
		time.sleep(0.2)

	import pdb; pdb.set_trace()


def get_positions(grid, N):
	valid_i, valid_j = np.where(~grid)
	idxs = np.random.choice(len(valid_i), N, replace=False)
	pos_i = valid_i[idxs]
	pos_j = valid_j[idxs]
	return np.stack((pos_i, pos_j), axis=1)


if __name__ == '__main__':
	main()