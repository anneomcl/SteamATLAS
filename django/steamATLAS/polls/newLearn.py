# -*- coding: utf-8 -*-
"""
Created on Wed Dec 03 14:47:37 2014

@author: CongJasonXu
"""

import numpy as np
#import sql_handler.gamesOwnedArray

STEPSIZE = 0.1


#Needs input of owned games + ike and dislike


def startLearn(L, w, theta):
    #i=0
    for l in L:
        if len(l) > 3:
            x = np.array(l[1: len(l) - 1])
            #print(l)
            #print(l[-1])
            w, theta = learn(np.array(w), theta, x, l[-1])
        #i+=1
    return list(w) + [theta]


def learn(w, theta, x, y):
    v = np.dot(w, x) + theta
    if v * y <= 0: # mistake; need update
        w += STEPSIZE * y * x
        theta += STEPSIZE * y
    return w, theta


#input W from  beofore ans x is single vector
def predict(w, x, theta): # w is weight vector for particular user
    data = x[1:]
    return np.dot(np.array(w), np.array(data)) + theta

'''
L = [
[29160, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
[33230, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
[30, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, -1],
[70, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, -1]
]

w = [0.0] * (len(L[0]) - 2)
theta = 0.0
combine = startLearn(L, w, theta)
#print combine
x = [107100, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
print predict(combine[: len(combine)-1], x, combine[-1])
'''
