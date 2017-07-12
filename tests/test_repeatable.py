import random
import r5


def test_repeatable():
    """Check that executions of walk with identical parameters yield the same results."""
    for i in range(100):
        seed = random.randint(0, 100000)
        n    = random.randint(0, 1000)

        assert r5.walk(n, seed=seed) == r5.walk(n, seed=seed)
