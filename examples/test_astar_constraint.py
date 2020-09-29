import numpy as np
from gridgym.Visualiser import *
from mapf.Grid import *
from mapf.Astar import *
import time


def main():
	size = 8
	grid = np.zeros((size,size)).astype(bool)

	env = Grid(grid)

	start = (1,1)
	end = (4,1)

	path = astar(env, start, end, constraint_fn)

	print("start: %s, end: %s" % (start, end))
	print(path)

	visualiser = Visualiser()

	for i in range(len(path)):
		visualiser.render(grid=grid, positions=np.array([path[i]]), goals=np.array([end]))
		time.sleep(0.2)


def constraint_fn(node, lastnode, t):
	if t==2 and node==(3,1):
		return False
	return True


if __name__ == '__main__':
	main()