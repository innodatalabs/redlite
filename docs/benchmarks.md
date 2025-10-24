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

## Math 500

[Math 500](https://huggingface.co/datasets/HuggingFaceH4/MATH-500) benchmark contains 500 math problems. Here is how to run this
benchmark in `redlite`:

```python
from redlite import run
from redlite.benchmark.math500 import dataset, metric

model = ...  # configure the model to be benchmarked

run(dataset=dataset, metric=metric, model=model)
```

## AIME 2024

[AIME 2024](https://huggingface.co/datasets/HuggingFaceH4/aime_2024) benchmark contains 30 math problems from
2024 [AIME I](https://artofproblemsolving.com/wiki/index.php/2024_AIME_I?srsltid=AfmBOoqP9aelPNCpuFLO2bLyoG9_elEBPgqcYyZAj8LtiywUeG5HUVfF)
and 2024 [AIME II](https://artofproblemsolving.com/wiki/index.php/2024_AIME_II_Problems/Problem_15) tests.

Here is how to run this benchmark in `redlite`:

```python
from redlite import run
from redlite.benchmark.aime24 import dataset, metric

model = ...  # configure the model to be benchmarked

run(dataset=dataset, metric=metric, model=model)
```

## AIME 2025

[AIME 2025](https://huggingface.co/datasets/MathArena/aime_2025) benchmark contains 30 math problems from
2025 [AIME I](https://artofproblemsolving.com/wiki/index.php/2025_AIME_I?srsltid=AfmBOop1d2rsYE_iQ79Ii436mnd68WCs1yYbDmseZ022jE3jOVNLVTI4)
and [AIME II](https://artofproblemsolving.com/wiki/index.php/2025_AIME_II_Problems?srsltid=AfmBOopHXUhbfAGeXYPn8Y2Ne1pDoSzw5FO-34N4krEG3GoCn-G7Bemk) tests.

Here is how to run this benchmark in `redlite`:

```python
from redlite import run
from redlite.benchmark.aime25 import dataset, metric

model = ...  # configure the model to be benchmarked

run(dataset=dataset, metric=metric, model=model)
```
