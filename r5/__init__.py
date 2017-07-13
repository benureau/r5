import argparse
import platform
import json
from datetime import datetime

from .walker import walk

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

    # get provenance
    provenance = {'python'   : {'implementation': platform.python_implementation(),
                                'version'       : platform.python_version_tuple(),
                                'compiler'      : platform.python_compiler(),
                                'branch'        : platform.python_branch(),
                                'revision'      : platform.python_revision()},
                  'platform' : platform.platform(),
                  'git_info' : _version.get_versions(),
                  'timestamp': datetime.utcnow().isoformat()+'Z',  # Z stands for UTC
                 }

    # random walk for n steps
    x = walk(args.n, seed=args.seed)

    # display & save results
    results = {'seed': args.seed, 'steps': args.n, 'walk': x,
               'provenance': provenance}
    for key in ['seed', 'steps', 'walk']:
        print('{}: {}'.format(key, results[key]))

    with open("r5_results_s{}_n{}.json".format(args.seed, args.n), "w") as fd:
        json.dump(results, fd)
