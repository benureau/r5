"""Just verifying that the code runs on a simple example.

`test_rerunnable()` is arguably redundant with and superseeded by other tests,
but this is also the easiest test to write: even if you don't write any
other test this one should be present. Moreover, even if you code because
unrepeatable, at least this test will pass.

It also provides a minimal example of how to use the code.

Other tests allow to test other ways to use the library.
"""
import r5


def test_rerunnable():
    """Return a walk of 10 elements"""
    return r5.walk(10, seed=1)

def test_rerunnable_full():
    """Return a walk of 10 elements, with provenance data"""
    return r5.walk_full(10, seed=1)

def test_rerunnable_main():
    """Test the function used for the `r5` command"""
    import os

    # looking for a result filename that does not exists on disk
    # this way, the test can create it and remove it without problem
    n, seed = 153, 351
    filename = "r5_results_s{}_n{}.json".format(seed, n)
    while os.path.isfile(filename):
        n += 1
        filename = "r5_results_s{}_n{}.json".format(seed, n)

    try:
        argv = ['r5', '--seed', str(seed), str(n)]
        r5.main(argv=argv)
    finally: # we clean up whether there was an error or not.
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass
