import numpy as np
from read_data import read_data
from lagmatrix import lagmatrix
#import pdb


def load_data(parameters):
	#pdb.set_trace()
	data = read_data()
	data = data / np.absolute(data).max()
	data_lag = lagmatrix(data, parameters.num_input)
	large = data_lag.shape[0] # porc_training = np.ceil(data.shape[0] * 0.8)
	large = np.ceil(large * 0.8) # Agregar a parameters
	data_training_x = data_lag[:int(large), :parameters.num_input]
	data_training_y = data_lag[:int(large), -1]#parameters.num_input]
	data_testing_x = data_lag[int(large):, :parameters.num_input]
	data_testing_y = data_lag[int(large):, -1]#parameters.num_input]
	
	# data_training_x, data_testing_y = lagmatrix(data, parameters.num_input)
	
	# data_training_x, data_training_y = lagmatrix(data[:L], parameters.num_input)
	# data_testing_x, data_testing_y = lagmatrix(data[L:], parameters.num_input)
	
	# data extr
	
	training = {'x': data_training_x, 'y': data_training_y}
	testing = {'x': data_testing_x, 'y': data_testing_y}
	return training, testing
	# return data_training_x, data_training_y, data_testing_x, data_testing_y
	