import numpy as np
from radial_spline import radial_spline
from scipy import stats
import matplotlib.pyplot as plt


def testing(testing_data, nest, parameters):
	t = nest[:parameters.num_input*parameters.hidden_nodes]
	d = nest[parameters.num_input*parameters.hidden_nodes:2*parameters.num_input*parameters.hidden_nodes]
	v = nest[2*parameters.num_input*parameters.hidden_nodes:]
	z = radial_spline(testing_data["x"], t, d, v, parameters)

	error = testing_data["y"] - z
	mse = np.mean(error**2)
	ape = np.absolute(error / testing_data["y"])
	mape = np.mean(ape) * 100

	slope, intercept, r_value, p_value, std_err = stats.linregress(z, testing_data["y"])

	sentido = 0

	for idx in range(z.shape[0] -1):
		if (testing_data["y"][idx+1] - testing_data["y"][idx] >= 0 and z[idx+1] - z[idx] >= 0) or (testing_data["y"][idx+1] - testing_data["y"][idx] < 0 and z[idx+1] - z[idx] < 0):
			sentido += 1

	sentido = sentido / (z.shape[0] - 1)

	print("mse {} mape {} r2 {} sentido {}".format(mse, mape, r_value**2, sentido))

	x = np.array(range(z.shape[0]))

	plt.plot(x, testing_data["y"], x, z)
	plt.show()
