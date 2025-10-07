from redlite._util import redlite_data_dir, read_runs
from collections import Counter

data_dir = redlite_data_dir()
runs = list(read_runs(data_dir))
print(f"Found {len(runs)} runs in {data_dir}")


multi_runs = {}
for run in runs:
    model = run["model"]
    dataset = run["dataset"]
    multi_runs.setdefault((model, dataset), []).sappend(run)

multi_runs = {k: len(v) for k, v in multi_runs.items() if len(v) > 1}

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, required=True, help='Model name')
    parser.add_argument('--dataset', type=str, required=True, help='Dataset name')
    args = parser.parse_args()

    

for (model, dataset), count in multi_runs.items():
    if count > 1:
        print(f"Model {model} on dataset {dataset} has {count} runs")
