import numpy as np


class Parameters():

	def __init__(
			self, num_input = 5, hidden_nodes = 3,
			dimension = 33, max_iterations = 50,
			num_nest = 70, pa = 0.4, max_run = 3):

		self.num_input = num_input #m
		self.hidden_nodes = hidden_nodes #H
		self.dimension = 2*num_input*hidden_nodes + hidden_nodes
		self.max_iterations = max_iterations
		self.num_nest = num_nest
		self.pa = pa
		self.nest = np.array([])
		self.max_run = max_run
		# parameters.nest = np.random.rand(parameters.num_nest, parameters.dimension)
		# self, num_input = 5, hidden_nodes = 3,
		# dimension = 33, max_iterations = 50,
		# num_nest = 70, pa = 0.4, max_run = 3):

