def simple_bounds(nest, lb, ub):
	nest[nest<lb] = lb[nest<lb]
	nest[nest>ub] = ub[nest>ub]
	return nest
