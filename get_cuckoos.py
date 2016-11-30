import numpy as np
from scipy.special import gamma
from simple_bounds import simple_bounds


def get_cuckoos(nests, best, lb, ub):
	beta = 3/2
	sigma = (gamma(1+beta)*np.sin(np.pi*beta/2)/(gamma((1+beta)/2)*beta*2**((beta-1)/2)))**(1/beta)
	new_nest = np.copy(nests)

	for idx, nest in enumerate(new_nest):
		u = np.random.randn(nest.shape[0]) * sigma
		v = np.random.randn(nest.shape[0])
		step = u / np.absolute(v)**(1/beta)
		step_size = 0.01*step*(nest - best)
		nest = nest + step_size*np.random.randn(nest.shape[0])
		new_nest[idx] = simple_bounds(nest, lb, ub)

	return new_nest
