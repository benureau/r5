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
    testdata_now = generate_testdata.compute_testdata()

    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, 'testdata.json'), 'r') as fd:
        testdata_reference = json.load(fd)

    assert testdata_now == testdata_reference
