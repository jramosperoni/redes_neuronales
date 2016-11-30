import csv
import operator
import numpy as np


def read_data(file_name='datos.csv'):

	array_data = np.array([])
	#array_data = []

	with open(file_name) as data_file:
		
		input_data = csv.reader(data_file)

		for register in input_data:
			if register:
				print(register[0])
				#array_data.append(register[0])
				array_data = np.append(array_data, round(float(register[0]), 2))

	return array_data.astype(float)

