# Built-in Metrics

## Match metric

Credits LLM answer iff it matches the expected one.

One can optionally choose to ignore casing and/or strip punctuation.

Matching can be done using the following strategies:

- `exact` (default): strings must be the same
- `prefix`: actual response should start with the expected sequence of words
- `contains`: actual response must contain the expected sequence of words

```python
from redlite.metric import MatchMetric

metric = MatchMetric(...)
```

Please see [Reference](../../reference/redlite/metric/) documentation for more detail and available parameters.

## BLEU metric

A sentence-level BLEU metric. One can choose one of `BLEU-1`, `BLEU-2`, `BLEU-3`, or `BLEU-4`

```python
from redlite.metric.bleu import BleuMetric

metric = BleuMetric(...)
```

For benchmarking CJK languages consider using `BleuCJKMetric`. The only difference is
in the tokenization --- CJK version will consider every character to be a separate token.

```python
from redlite.metric.bleu import BleuCJKMetric

metric = BleuCJKMetric(...)
```

Please see [Reference](../../reference/redlite/metric/bleu/) documentation for more detail and available parameters.

## ROUGE metric

A standard ROUGE metric. One can choose one of `rougeL`, `rouge1`, or `rouge2`.

```python
from redlite.metric.rouge import RougeMetric

metric = RougeMetric(...)
```

For benchmarking in CJK languages consider using `RougeCJKMetric`. The only difference is
in the tokenization --- CJK version will consider every character to be a separate token.

```python
from redlite.metric.rouge import RougeCJKMetric

metric = RougeCJKMetric(...)
```

Please see [Reference](../../reference/redlite/metric/rouge/) documentation for more detail and available parameters.

## F1 on word set metric

Computes F1 metric on the tokenized sets of `expected` and `actual` strings.

```python
from redlite.metric.f1 import F1Metric

metric = F1Metric(...)
```

Please see [Reference](../../reference/redlite/metric/f1/) documentation for more detail and available parameters.

## Boxed Math metrics

This metric is specific to [Math500 benchmark](../benchmarks). It scores answers to math tests, that are expected to be within a
LaTeX `\boxed{...}` function.

```python
from redlite.metric.math import BoxedMathMetric

metric = BoxedMathMetric()
```

Please see [Reference](../../reference/redlite/metric/math/) documentation for more detail and available parameters.

## Live Code Bench metric

This metric is specific to the [LiveCodeBench](../benchmarks). It scores python code generation. It requires that
a server application `redlite-livecodebench-grader` is running as a docker container:

```bash
docker run -it -p 8000:80 ilabs/redlite-livecodebench-grader
```

If you use a different endpoint for hosting the grader, change `endpoint` parameter to the
`LiveCodeBench` constructor accordingly (default endpoint is `http://localhost:8000`)

Example:

```python
from redlite.metric.livecodebench import LiveCodeBenchMetric

metric = LiveCodeBenchMetric(endpoint="http://grader.example.com:9999")
```

Please see [Reference](../../reference/redlite/metric/livecodebench/) documentation for more detail and available parameters.

## Best of several metrics

We may want to score LLM answer with several metrics and choose the best score. For example, when we score an item with
the expected answer `"I refuse to tell you this"` one may want to use `MatchMetric(strategy="prefix")`. And for the data points that
expect model to give a thoughtful answer, we want to use `RougeMetric(rouge_type="rouge2")`.
The good dataset metric in this case is `BestOf`.

```python
prefix_metric = MatchMetric(strategy="prefix")
rouge2_metric = RougeMetric(rouge_type="rouge2")

metric = BestOfMetric(prefix_metric, rouge2_metric)
```

Please see [Reference](../../reference/redlite/metric/) documentation for more detail.

## Custom metrics

Custom metrics can be easily integrated, see the [Customization Guide](custom.md).
