"""A simple example on how to use the code"""
import dotdot
import walk


n, seed = 10, 1
print('Random walk with {} steps (random seed={}):'.format(n, seed))
print(walk.walk(n, seed=seed))
