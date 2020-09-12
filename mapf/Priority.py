from mapf.Astar import *

def priority(env, starts, goals):
	constraints = {}
	paths = []
	for start, goal in zip(starts, goals):
		def constraint_fn(node, t):
			return node not in constraints.get(t, set())
		path = astar(env, start, goal, constraint_fn)
		paths.append(path)
		for t, node in enumerate(path):
			if t in constraints:
				constraints[t].add(node)
			else:
				constraints[t] = set([node])
	return paths