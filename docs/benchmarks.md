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

## Live Code Bench code generation

[LiveCodeBench](https://huggingface.co/datasets/lighteval/code_generation_lite) benchmark contains Pyhton code generation tasks.
Here is how to run this benchmark in `redlite`.

First, you need to run grader service with docker. You may need to build the docker first, see
GitHub project [redlite-livecodebench-grader](https://github.com/innodatalabs/redlite-livecodebench-grader) for details.
Once you have Docker image, start grading service:

```bash
docker run -it -p 8000:80 ilabs/redlite-livecodebench-grader:latest
```

Now you can run benchmark like this:

```python
from redlite import run
from redlite.benchmark.livecodebench import get_dataset, get_metric

model = ...  # configure the model to be benchmarked

dataset = get_dataset()  # use default partition
metric = get_metric()  # use default grader endpoint http://localhost:8000

run(dataset=dataset, metric=metric, model=model)
```

There are 4 available test configs (a.k.a. partitions):

| Name              | Start Date | End Date | Revision | Records |
|-------------------|------------|----------|----------|---------|
| test_v5_2408_2502 | 2024-08    | 2025-02  | v5       | 279     |
| test_v5_2407_2412 | 2024-07    | 2024-12  | v5       | 315     |
| test_v5_2410_2502 | 2024-10    | 2025-02  | v5       | 166     |
| test_v6_2408_2505 | 2024-08    | 2025-05  | v6       | 454     |

Default config is `test_v5_2408_2502`. You may load other configs by passing config name to the `get_dataset` function.

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
