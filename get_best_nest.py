import numpy as np
from radial_spline import radial_spline


def get_best_nest(nests, new_nest, fitness, parameters, training_data):
	for idx, nest in enumerate(new_nest):
		t = nest[:parameters.num_input*parameters.hidden_nodes]
		d = nest[parameters.num_input*parameters.hidden_nodes:2*parameters.num_input*parameters.hidden_nodes]
		v = nest[2*parameters.num_input*parameters.hidden_nodes:]
		z = radial_spline(training_data["x"], t, d, v, parameters)
		error = training_data["y"] - z
		new_fitness = np.mean(error**2)
		if new_fitness <= fitness[idx]:
			fitness[idx] = new_fitness
			nests[idx] = nest
			
	min_fitness, best = np.amin(fitness), nests[np.argmin(fitness)]
	return min_fitness, best, nests, fitness
	#t = nest(:parameters.num_input*parameters.hidden_nodes)
	#d = nest(parameters.num_input*parameters.hidden_nodes+1:2*parameters.num_input*parameters.hidden_nodes)
	#v = nest(2*parameters.num_input*parameters.hidden_nodes+1:)