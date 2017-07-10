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



if __name__ == '__main__':

    # Random walk for 10 steps
    seed = 1
    random.seed(seed)
    x = walk(10)

    # Display & save results
    print(x)
    with open("results-R3-%d.txt" % seed, "w") as file:
        file.write(str(x))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser("Random walk")
    parser.add_argument('--seed', type=int, default=1,
                        help='Seed for random number generator ')
    parser.add_argument('n', type=int, default=10,
                        help='Number of step(s) to walk')
    args = parser.parse_args()

    # Random walk for n steps
    x = walk(rng(args.seed), args.n)

    # Display & save results
    print("Seed:", args.seed)
    print("Number of steps:", args.n)
    print("Result:",  x)
    with open("results-R5-%d.txt" % seed, "w") as file:
        file.write("Version: R5")
        file.write("Seed: %d" % args.seed)
        file.write("Steps number: %d" % args.n)
        file.write("Output: %s" % str(x))
