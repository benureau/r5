import json
import r5


n, seed = 10, 1

results = r5.walk_full(10, seed=1, dirty=False)

with open("r5_results_s{}_n{}.json".format(args.seed, args.n), "w") as fd:
    json.dump(results, fd)

for key in results.keys():
    print('{}: {}'.format(key, results[key]))
