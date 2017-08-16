import os
import json

import generate_testdata
import r5


def test_reproducible_hardcoded():
    """Check that walk is producing the same sequence as previous version of the code."""
    expected = [0, -1, 0, 1, 0, -1, -2, -1, 0, -1, -2]
    actual   = r5.walk(10, seed=1)
    assert expected == actual, '{} (expected) != {} (actual)'.format(expected, actual)


def test_reproducible():
    """Check that walk is producing the same sequence as previous version of the code."""
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, 'testdata.json'), 'r') as fd:
        testdata_reference = json.load(fd)

    for testrun in testdata_reference:
        # the parameters are extracted from the provenance data accompanying the results
        n    = testrun['parameters']['n']
        seed = testrun['parameters']['seed']
        walk_now = r5.walk(n, seed=seed)
        assert list(walk_now) == list(testrun['results'])
