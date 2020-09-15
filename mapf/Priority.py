from mapf.Astar import *

def priority(env, starts, goals):
	constraints = {}
	steady_state_constraints = {}
	paths = []
	for start, goal in zip(starts, goals):
		def constraint_fn(node, lastnode, t):
			overlap = node in constraints.get(t, set())
			swap = (lastnode in constraints.get(t, set())) and (node in constraints.get(t-1, set()))
			ss_overlap = False
			for ss_node, t_func in steady_state_constraints.items():
				if ss_node==node and t_func(t):
					ss_overlap = True
					break
			return not (overlap or swap or ss_overlap)
		path = astar(env, start, goal, constraint_fn)
		paths.append(path)
		if path is not None:
			for t, node in enumerate(path):
				if t in constraints:
					constraints[t].add(node)
				else:
					constraints[t] = set([node])
			t_end = len(path)-1
			node_end = path[-1]
			steady_state_constraints[node_end] = lambda t: t >= t_end
		else:
			steady_state_constraints[start] = lambda t: t >= 0
	return paths