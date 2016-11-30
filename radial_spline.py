import numpy as np
#import pdb


def radial_spline(data, t, d, v, parameters):
	t = np.reshape(t, (parameters.hidden_nodes, parameters.num_input))
	d = np.reshape(d, (parameters.hidden_nodes, parameters.num_input))
	output_hidden_nodes = np.array([], dtype=float).reshape(0, parameters.hidden_nodes)

	#pdb.set_trace()

	for item in data:
		#np.linalg.norm((item - t) / d, axis=1)
		output_hidden_nodes = np.vstack((output_hidden_nodes, [np.sqrt(1 + (np.linalg.norm((item - t) / d, axis=1))**2)]))

	return np.dot(output_hidden_nodes, v)
