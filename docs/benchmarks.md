# Built-in Benchmarks

Benchmark is a combination of dataset and metric. We provide several popular benchmarks out-of-box.

## MMLU-Pro

[MMLU Pro](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro) benchmark contains 12036 difficult multiple-choice questions
from the realm of math, chemistry, engineering, etc.

Here is how to run it with `redlite`:

```python
from redlite import run
from redlite.benchmark.mmlu_pro import dataset, metric

model = ...  # configure the model to be benchmarked

run(dataset=dataset, metric=metric, model=model)
```
