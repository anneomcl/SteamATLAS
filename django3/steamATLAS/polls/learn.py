import numpy as np
#import sql_handler.gamesOwnedArray

STEPSIZE = 0.1


#Needs input of owned games + ike and dislike


def startLearn(L, w, theta):
    returnArray=[]
    w = np.array([0.0] * (len(L[0]) - 2) + [1.0])
    for l in L:
        if len(l) > 3:
            #print(l)
            x = np.array(l[1: len(l) - 1] + [0.0])
            w = learn(w, x, l[-1])
            #print(x)
            #print(w)
    returnArray.append(w)
    returnArray.append(theta)
    return returnArray


def learn(w, x, y):
	#v = np.dot(w, x)
	#if v * y <= 0: # mistake; need update
    #	w += STEPSIZE * y * x
	return w


#input W from  beofore ans x is single vector
def predict(w, x, theta): # w is weight vector for particular user
	return np.dot(np.array(w), np.array(x + [0.0]))
