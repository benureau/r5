# Copyright (c) 2017 Nicolas P. Rougier and Fabien C. Y. Benureau
# Release under the BSD 2-clause license
# Tested with CPython 3.6.1 / macOS 10.12.4 / 64 bits architecture
import random

def walk(n, seed=1):
    """
    Generate a random walk.

    The walk is initialized at zero, and this initial state is included in
    the walk.

    :param n:     the number of steps of the walk.
    :param seed:  the seed of for the random number generator. Each walk has an
                  independent random number generator.
    """
    # we create an independent RNG for the function
    rng = random.Random()
    rng.seed(seed)

    steps = [0]
    for i in range(n):
        if rng.uniform(-1,+1) < 0:
            steps.append(steps[-1] - 1)
        else:
            steps.append(steps[-1] + 1)
    return steps
