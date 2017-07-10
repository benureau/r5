import random

import dotdot
import walk


def test_repeatable():
    """Check that executions of walk with identical parameters yield the same results."""
    for i in range(100):
        seed = random.randint(0, 100000)
        n    = random.randint(0, 1000)

        assert walk.walk(n, seed=seed) == walk.walk(n, seed=seed)
