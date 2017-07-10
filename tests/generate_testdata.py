"""This script generate the test data used in test_reproducible.

We use JSON rather than a binary format such as pickle, for two reasons:
* it can be read by human
* it can be read by other language easily, thus creating data to that can be
  compared against in the context of a replication effort.
"""
import json

import dotdot
import walk


def compute_testdata():
    """Generate the data to test"""
    return [walk.walk(28, seed= 0),
            walk.walk(47, seed= 1),
            walk.walk(99, seed=99)]

def save_testdata(data):
    """Write the test data to disk."""
    with open('testdata.json', 'w') as fd:
        json.dump(data, fd)


if __name__ == '__main__':
    test_data = compute_testdata()
    save_testdata(test_data)
