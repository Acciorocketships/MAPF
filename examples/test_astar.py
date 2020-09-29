import numpy as np
from gridgym.Visualiser import *
from mapf.Grid import *
from mapf.Astar import *
import time

size = 16
grid = np.random.rand(size, size) < 0.3

env = Grid(grid)

start = tuple(np.random.randint(size, size=2))
end = tuple(np.random.randint(size, size=2))
while grid[start[0],start[1]] or grid[end[0],end[1]]:
	start = tuple(np.random.randint(size, size=2))
	end = tuple(np.random.randint(size, size=2))

path = stay(env, start, end, T=20)

print("start: %s, end: %s" % (start, end))
print(path)

visualiser = Visualiser()

for i in range(len(path)):
	visualiser.render(grid=grid, positions=np.array([path[i]]), goals=np.array([end]))
	time.sleep(0.2)

time.sleep(3)