"""This script generate the test data used in test_reproducible.

We use JSON rather than a binary format such as pickle, for two reasons:
* it can be read by human
* it can be read by other language easily, thus creating data to that can be
  compared against in the context of a replication effort.
"""
import json
import os

import r5


def compute_testdata():
    """Generate the data to test"""
    return [r5.walk_full(28, seed= 0, dirty=False),
            r5.walk_full(47, seed= 1, dirty=False),
            r5.walk_full(99, seed=99, dirty=False)]

def save_testdata(data):
    """Write the test data to disk."""
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, 'testdata.json'), 'w') as fd:
        json.dump(data, fd)


if __name__ == '__main__':
    test_data = compute_testdata()
    save_testdata(test_data)
