import numpy as np

STEPSIZE = 0.1

def startLearn(L):
	# initialize w
	w = np.array([0.0] * (len(L[0]) - 2) + [1.0])
	for l in L:
		# construct x: remove appId, separate y
		x = np.array(l[1: len(l) - 1] + [0.0])
		w = learn(w, x, l[-1])
		print w

def learn(w, x, y):
	v = np.dot(w, x)
	if v * y <= 0: # mistake; need update
		w += STEPSIZE * y * x
	return w


L = [[123, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], [123, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]]
# input L is a list of list
startLearn(L)