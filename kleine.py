#!/usr/bin/env python2

# //iamtrask.github.io/2015/07/12/basic-python-network

import numpy as np


X = np.array([ [0,0,1]
             , [0,1,1]
             , [1,0,1]
             , [1,1,1]
             ])

sigmoid = lambda x: 1 / (1 + np.exp(- x))
sigmoid_prime = lambda x: x * (1 - x)


# Seed so that each run has the same starting state
np.random.seed(1)

def nn__3_1 (l0, lminus1):
    w0 = 2 * np.random.random((3, 1)) -1
    for j in xrange(6 * 1000):
        l1 = sigmoid(np.dot(l0, w0))
        l1_delta = sigmoid_prime(l1) * (lminus1 - l1)
        w0 += np.dot(l0.T, l1_delta)
    print l1

def nn__3_4_1 (l0, lminus1):
    w0 = 2 * np.random.random((3, 4)) -1
    w1 = 2 * np.random.random((4, 1)) -1
    for j in xrange(10 * 1000):
        l1 = sigmoid(np.dot(l0, w0))
        l2 = sigmoid(np.dot(l1, w1))
        l2_delta = sigmoid_prime(l2) * (lminus1 - l2)
        l1_delta = sigmoid_prime(l1) * np.dot(l2_delta, w1.T)
        w1 += np.dot(l1.T, l2_delta)
        w0 += np.dot(l0.T, l1_delta)
    print l2



y31 = np.array(
    [ [0]
    , [0]
    , [1]
    , [1]
    ])

y341 = np.array(
    [ [0]
    , [1]
    , [1]
    , [0]
    ])


print 31
nn__3_1(X, y31)

np.random.seed(1)

print 341
nn__3_4_1(X, y341)
