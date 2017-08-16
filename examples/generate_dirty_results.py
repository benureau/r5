"""Same as `generate_results.py`, expect does not check for a clean git repository."""
import json
import r5

n, seed = 10, 1
results = r5.walk_full(10, seed=1, dirty=True)

with open("r5_results_n{}_s{}_dirty.json".format(seed, n), "w") as fd:
    json.dump(results, fd)

for key in results.keys():
    print('{}: {}'.format(key, results[key]))
