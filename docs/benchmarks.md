# Built-in Benchmarks

Benchmark is a combination of dataset and metric. We provide several popular benchmarks out-of-box.

## MMLU-Pro

[MMLU Pro](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro) benchmark contains 12032 difficult multiple-choice questions
from the realm of math, chemistry, engineering, etc.

Here is how to run it with `redlite`:

```python
from redlite import run
from redlite.benchmark.mmlu_pro import dataset, metric

model = ...  # configure the model to be benchmarked

run(dataset=dataset, metric=metric, model=model)
```

## GPQA

[GPQA](https://huggingface.co/datasets/Idavidrein/gpqa) benchmark contains four separate datasets of multiple-choice questions:

* `main` - 448 rows
* `diamon` - 198 rows
* `experts` - 60 rows
* `extended` - 546 rows

Here is how to run `diamond` version with `redlite`:

```python
from redlite import run
from redlite.benchmark.gpqa import get_dataset, metric

model = ...  # configure the model to be benchmarked

dataset = get_dataset('diamond')

run(dataset=dataset, metric=metric, model=model)
```
