import numpy as np
from random import choices

P = np.array([[0.6, 0.2, 0.2],
              [0.7, 0.1, 0.2],
              [0.6, 0.2, 0.2]])

state = np.array([[0.0, 1.0, 0.0]])

for i in range(10):
	prob = np.dot(state, P)[0]
	s = choices([1, 2, 3], weights=prob)
#	print(prob)
#	print(s)
	if s[0] == 1:
		state = np.array([[1.0, 0.0, 0.0]])
	elif s[0] == 2:
		state = np.array([[0.0, 1.0, 0.0]])
	else:
		state = np.array([[0.0, 0.0, 1.0]])
	print(state)
