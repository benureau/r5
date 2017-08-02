"""Just verifying that the code runs on a simple example.

`test_rerunnable()` is arguably redundant with and superseeded by other tests,
but this is also the easiest test to write: even if you don't write any
other test this one should be present. Moreover, even if you code because
unrepeatable, at least this test will pass.

It also provides a minimal example of how to use the code.
"""
import r5


def test_rerunnable():
    """Return a walk of 10 elements"""
    return r5.walk(10, seed=1)

def test_rerunnable_full():
    """Return a walk of 10 elements, with provenance data"""
    return r5.walk_full(10, seed=1, dirty=True)
