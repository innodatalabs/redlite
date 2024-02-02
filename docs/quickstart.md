# Quick start

Best way to learn `redlite` api is to run few scripts. Lets do it!

## Overview

1. Install `redlite` and dependencies
2. Write your script
    * Load dataset from HuggingFace
    * Define your own model
    * Define your own metric
    * Call the `run` function
3. Run the benchmark
4. Review the results

## Installation

```bash
python3.11 -m venv .venv
. .venv/bin/activate
pip install redlite[all]
```

_Note: we've chosen to install `all` dependencies for simplicity. In production we advise
to load only necessary components, to avoid bloat and transitive dependency conflicts._

## Write your script

Create a `*.py` file.
You may check [samples](http://github.com/innodatalabs/redlite/tree/master/samples) for inspiration.

Here we will write the one from scratch.

### Load dataset from HuggingFace

First, import `load_dataset` function and call it to download a dataset:

```python
from redlite import load_dataset

dataset = load_dataset('hf:innodatalabs/rt-factcc')
```

This loads the dataset from <https://huggingface.co/datasets/innodatalabs/rt-factcc>.

### Define your model

We will create a simple model that always says `"Hello, humans! I am alive!"`, regardless of the
context.

```python
from redlite import NamedModel

def happy(messages):
    return "Hello, humans! I am alive!"

model = NamedModel('happy', happy)
```

We first defined a function that takes the conversation (which is a list of messages),
and produces the response string.

Then we created a model and gave it name `"happy"`, and passed our function as the second argument.

_Note: it is important to be disciplined when naming the models. Analytical tools of redlite
identify models by their names. If two different models have the same name grouping and score aggregations
will be messed up._

### Define your metric

Metric is a function that takes `expected` string and `actual` mode response and grades the response against the
expected one, returning a number from 0.0 (bad) to 1.0 (great).

```python
from redlite import NamedMetric

def score(expected, actual):
    if expected == actual:
        return 1.0
    if 'happy' in actual:
        return 0.5
    return 0.0

metric = NamedMetric('simple-metric', score)
```

We first defined a function that computes the score.

Then we created a metric object with name `"simple-metric"` and passed scoring function as second argument.

_Note: it is important to be disciplined when naming your metrics. Make sure that metric name is unique.
Just like with model naming, analytical tools consider name as metric identity. Having two different metrics
use the same name will bring havoc into the analytis._

### Call the `run` function

Finaly, we take `dataset`, `model` and `metric` and pass them to the `run()` function.

Here is the complete script:

```python
from redlite import load_dataset, NamedModel, NamedMetric

dataset = load_dataset('hf:innodatalabs/rt-factcc')

def happy(messages):
    return "Hello, humans! I am alive!"

model = NamedModel('happy', happy)

def score(expected, actual):
    if expected == actual:
        return 1.0
    if 'happy' in actual:
        return 0.5
    return 0.0

metric = NamedMetric('simple-metric', score)

run(
    model=model,
    dataset=dataset,
    metric=metric,
)
```

## Run the benchmark

To run the benchmark just execute the script.
Assuming that we named script file `my_script.py`, here is the command:

```bash
python my_script.py
```

You should see it running. Since the model is pretty much fake, and metric
computation is very light, the benchmark will finish in few seconds.

You may get the following output on your terminal screen:

```text
RedLite run forward-coordinator-1:
        model  : happy
        dataset: hf:innodatalabs/rt-factcc
        metric : simple-metric
100%|█████████████████████| 100/100 [00:00<00:00, 382.20it/s]
Smile! All done!
```

## Review the results

```bash
redlite server
```

This command will start server on port `8000`. Open your browser and navigate to <http://localhost:8000>.

You should now see the UI.
