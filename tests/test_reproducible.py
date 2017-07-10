import json
import generate_testdata
from walk import walk


def test_reproducible_hardcoded():
    """Check that walk is producing the same sequence as previous version of the code."""
    print(walk(10,seed=1))
    assert walk(10, seed=1) == [0, -1, 0, 1, 0, -1, -2, -1, 0, -1, -2]


def test_reproducible():
    """Check that walk is producing the same sequence as previous version of the code."""
    testdata_now = generate_testdata.compute_testdata()

    with open('./testdata.json', 'r') as fd:
        testdata_reference = json.load(fd)

    assert testdata_now == testdata_reference
