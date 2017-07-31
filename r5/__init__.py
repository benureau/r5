import os
import argparse
import json

from .walker import walk, walk_full
from .provenance import provenance

# versioneer
from . import _version
__version__ = _version.get_versions()['version']


def main():
    """Entry point for the `r5` console script"""
    # handling command line arguments
    parser = argparse.ArgumentParser("Random walk")
    parser.add_argument('--seed', type=int, default=1,
                        help='seed for random number generator ')
    parser.add_argument('n', type=int, default=10,
                        help='number of step(s) to walk')
    args = parser.parse_args()

    # random walk for n steps
    results = walk_ful(args.n, seed=args.seed)

    # display & save results
    with open("r5_results_s{}_n{}.json".format(args.seed, args.n), "w") as fd:
        json.dump(results, fd)
    for key in result.keys():
        print('{}: {}'.format(key, results[key]))

def test():
    """Run all the tests in the `tests/` directory using pytest """
    import pytest
    here = os.path.abspath(os.path.dirname(__file__))
    pytest.main([os.path.join(here, 'tests')])
