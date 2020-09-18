from mapf.Astar import *

def priority(env, starts, goals):
	paths = [None] * len(starts)
	T = 0
	redo = range(len(starts))
	while len(redo) > 0:
		constraints = {}
		changed = False
		for agent in redo:
			path = compute_paths(env, starts[agent], goals[agent], constraints, T)
			t = len(path)-1
			if t > T:
				print(t, T)
				T = t
				redo = range(agent)
				changed = True
			paths[agent] = path
		if not changed:
			redo = range(0)
	return paths


def compute_paths(env, start, goal, constraints, T):
	def constraint_fn(node, lastnode, t):
		overlap = node in constraints.get(t, set())
		swap = (lastnode in constraints.get(t, set())) and (node in constraints.get(t-1, set()))
		return not (overlap or swap)
	path = astar(env, start, goal, constraint_fn)
	t = len(path)-1
	hold_path = stay(env=env, start=path[-1], goal=goal, constraint_fn=constraint_fn, start_t=t, T=T)
	path = path + hold_path[1:]
	for t, node in enumerate(path):
		if t in constraints:
			constraints[t].add(node)
		else:
			constraints[t] = set([node])
	return path