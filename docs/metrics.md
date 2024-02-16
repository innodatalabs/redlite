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

## Custom metrics

Custom metrics can be easily integrated, see the [Customization Guide](custom.md).
