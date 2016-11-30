import numpy as np
from get_cuckoos import get_cuckoos
from get_best_nest import get_best_nest
from empty_nests import empty_nests
#import pdb


def cuckoo_search(parameters, training, run):
	lower_bound = -1 * np.ones(parameters.dimension)
	upper_bound = 1 * np.ones(parameters.dimension)
	
	#pdb.set_trace()
	#nest = np.random.rand(parameters.num_nest, parameters.dimension)
	#nests = np.random.uniform(0, 1, (parameters.num_nest, parameters.dimension))
	nests = np.random.uniform(size=(parameters.num_nest, parameters.dimension))
	
	# aplicar enumerate
	#print("1")
	#print(nests)
	for idx, nest in enumerate(nests):
		nests[idx] = lower_bound + (upper_bound - lower_bound)*np.random.uniform(size=parameters.dimension)

	#print("2")
	#print(nests)
		
	fitness = 10**10 * np.ones(parameters.num_nest)
	min_fitness, best_nest, nests, fitness = get_best_nest(nests, nests, fitness, parameters, training)
	
	mse = np.array([], dtype=float)
	
	for iteration in range(1, parameters.max_iterations + 1):
		new_nests = get_cuckoos(nests, best_nest, lower_bound, upper_bound)
		new_fitness, best, nests, fitness = get_best_nest(nests, new_nests, fitness, parameters, training)

		new_nests = empty_nests(nests, lower_bound, upper_bound, parameters)
		new_fitness, best, nests, fitness = get_best_nest(nests, new_nests, fitness, parameters, training)

		if new_fitness < min_fitness:
			min_fitness = new_fitness
			best_nest = best

		mse = np.append(mse, min_fitness)
		print("run {} iteration {} mse {}".format(run, iteration, min_fitness))

	return min_fitness, best_nest
