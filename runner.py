# time
import numpy as np
from parameters import Parameters
from carga import load_data
from cuckoo_search import cuckoo_search
from testing import testing


def runner():
	parameters = Parameters()
	training_data, testing_data = load_data(parameters)
	# dict for metrics
	# dict for nests

	for run in range(1, parameters.max_run + 1):
		# trn
		min_fitness, best_nest = cuckoo_search(parameters, training_data, run)
		# append(min_fitness)
		# tst
		testing(testing_data, best_nest, parameters)
		# metrics
		# nests

if __name__ == '__main__':
	runner()
