# versioneer
from . import _version
__version__ = _version.get_versions()['version']


from .walker import walk


def main():
    """Entry point for the `r5` console script"""
    # handling command line arguments
    import argparse
    parser = argparse.ArgumentParser("Random walk")
    parser.add_argument('--seed', type=int, default=1,
                        help='seed for random number generator ')
    parser.add_argument('n', type=int, default=10,
                        help='number of step(s) to walk')
    args = parser.parse_args()

    # random walk for n steps
    x = walk(args.n, seed=args.seed)

    # display & save results
    import json
    results = {'seed': args.seed, 'steps': args.n, 'walk': x}
    for key in ['seed', 'steps', 'walk']:
        print('{}: {}'.format(key, results[key]))

    with open("r5_results_s{}_n{}.json".format(args.seed, args.n), "w") as fd:
        json.dump(results, fd)
