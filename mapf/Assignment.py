from munkres import Munkres
from mapf.Astar import *
import numpy as np

class Assignment:

	@staticmethod
	def compute_matrix(env, starts, goals):
		env = env
		starts = starts
		goals = goals
		costmat = np.zeros((len(starts),len(goals)))
		for i, start in enumerate(starts):
			for j, goal in enumerate(goals):
				_, cost = astar(env=env, start=start, goal=goal, return_cost=True)
				costmat[i,j] = cost
		return costmat

	@staticmethod
	def hungarian(costmat):
		stuck_mask = np.all(costmat==float('inf'), axis=1)
		costmat[stuck_mask,:] = 0
		m = Munkres()
		idx_pairs = m.compute(costmat)
		idxs = np.array(list(map(lambda e: e[1], idx_pairs)))
		return idxs

	@staticmethod
	def action(env, starts, goals, assignment=None):
		if assignment is not None:
			goals = goals[assignment]
		actions = np.zeros((len(starts), 2))
		for i in range(len(starts)):
			path = astar(env=env, start=starts[i], goal=goals[i])
			if len(path) >= 2:
				actions[i,:] = np.array(path[1]) - np.array(path[0])
		return actions