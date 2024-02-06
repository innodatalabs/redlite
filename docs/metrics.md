# Built-in Metrics

## Exact metric

Credits LLM answer iff it is the same as the expected one.

One can optionally choose to ignore casing, strip punctuation, and normalize whitespace.

```python
from redlite.metric import ExactMetric

metric = ExactMetric(...)
```

## Prefix metric

Credits LLM answer iff it starts with the expected string.

One can optionally choose to ignore casing, strip punctuation, and normalize whitespace.

```python
from redlite.metric import PrefixMetric

metric = PrefixMetric(...)
```

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

## F1 on word set metric

Computes F1 metric on the tokenized sets of `expected` and `actual` strings.

```python
from redlite.metric.f1 import F1Metric

metric = F1Metric(...)
```

## Custom metrics

Custom metrics can be easily integrated, see the [Customization Guide](custom.md).
