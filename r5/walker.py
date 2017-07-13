# Copyright (c) 2017 Nicolas P. Rougier and Fabien C. Y. Benureau
# Release under the BSD 2-clause license
# Tested with CPython 3.6 / macOS 10.12.4 / 64 bits architecture
import random

def walk(n, seed=1):
    """ Random walk for n steps """
    rng = random.Random() # we create an independent RNG for the function
    rng.seed(seed)

    steps = [0]
    for i in range(n):
        if rng.uniform(-1,+1) < 0:
            steps.append(steps[-1] - 1)
        else:
            steps.append(steps[-1] + 1)
    return steps



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


# before install, you can call `python r5.py`
# after install, you can simply call `r5`
if __name__ == '__main__':
    main()
