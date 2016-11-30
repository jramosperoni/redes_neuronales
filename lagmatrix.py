import numpy as np
from scipy.ndimage.interpolation import shift


def lagmatrix(matrix, lag):
	# verificar que lag no sea mayor que largo lista
	matrix_aux = matrix[:]

	for index in range(1, lag + 1):
		matrix_aux = np.vstack((shift(matrix, index), matrix_aux))

	return matrix_aux.T[lag:]

