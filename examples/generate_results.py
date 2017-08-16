import json
import r5


# compute results and retrieve provenance data
n, seed = 10, 1
results = r5.walk_full(10, seed=1, dirty=False)

# save result to disk
with open("r5_results_s{}_n{}.json".format(seed, n), "w") as fd:
    json.dump(results, fd)

# print results
for key in results.keys():
    print('{}: {}'.format(key, results[key]))
