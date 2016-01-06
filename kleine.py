#!/usr/bin/env python2

# //iamtrask.github.io/2015/07/12/basic-python-network

import numpy as np


X = np.array([ [0,0,1]
             , [0,1,1]
             , [1,0,1]
             , [1,1,1]
             ])
y = np.array([ [0]
             , [0]
             , [1]
             , [1]
             ])

sigmoid = lambda x: 1 / (1 + np.exp(- x))
sigmoid_prime = lambda x: x * (1 - x)


# Seed so that each run has the same starting state
np.random.seed(1)

# Init weights randomly with mean 0
syn0 = 2 * np.random.random((3, 1)) -1
# syn0 = 2 * np.random.random((3, 4)) -1
# syn1 = 2 * np.random.random((4, 1)) -1

l0 = X
for j in xrange(10 * 1000):
    # Forward propagation
    l1 = sigmoid(np.dot(l0, syn0))

    # Back propagation
    l1_error = y - l1
    l1_delta = sigmoid_prime(l1) * l1_error
    syn0 += np.dot(l0.T, l1_delta)

    # #y = 0 1 1 0 .T
    # l1 = sigmoid(np.dot(l0, syn0))
    # l2 = sigmoid(np.dot(l1, syn1))
    # l2_delta = sigmoid_prime(l2) * (y - l2)
    # l1_delta = sigmoid_prime(l1) * np.dot(l2_delta, syn1.T)
    # syn1 += np.dot(l1.T, l2_delta)
    # syn2 += np.dot(l0.T, l1_delta)

print "Layer1:"
print l1
