import numpy as np
from simple_bounds import simple_bounds


def empty_nests(nests, lb, ub, parameters):
	discovered = np.random.uniform(size=nests.shape) > parameters.pa
	step_size = np.random.uniform()*(nests[np.random.permutation(parameters.num_nest)] - nests[np.random.permutation(parameters.num_nest)])
	new_nest = nests + step_size*discovered
	
	for idx, nest in enumerate(new_nest):
		new_nest[idx] = simple_bounds(nest, lb, ub)
		
	return new_nest
