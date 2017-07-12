"""A simple example on how to use the code"""
import r5


n, seed = 10, 1
print('Random walk with {} steps (random seed={}):'.format(n, seed))
print(r5.walk(n, seed=seed))
