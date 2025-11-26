# Parallel runs (advanced)

In certain environments runs can be accelerated by running LLM queries in parallel with `parallel_run`.

With `parallel_run` we will create multiple worker processes, each creating its own instance of model and metric. Dataset records are
distributed evenly between these workers.

Please note that not all models and not all metrics can be used in parallel. For example, if model grabs GPU resources of the local
machine, attempt to run this in parallel will likely exhaust GPU memory and crash. Practically, `parallel_run` works best for cloud-based
LLM providers, or running an `vLLM` server locally and talking to it using cloud-based model with local endpoint.

Here is a sample of using `parallel_run` method:

```python
from redlite import parallel_run
from redlite.benchmark.math500 import metric, dataset
from redlite.model.openai_model import OpenAIModel
import os

api_key = os.environ["OPENAI_API_KEY"]

model_producer = lambda: OpenAIModel(model="gpt-4o", api_key=api_key)
metric_producer = lambda: metric

parallel_run(dataset=dataset, model_producer=model_producer, metric_producer=metric_producer)
```

Note that unlike `run`, we do not pass `model` and `metric` directly to the `parallel_run` function. Instead, we pass
functions that workers will invoke to instantiate their copies of model and metric.

You can control parallelism by passing `num_workers` argument to the `parallel_run` function. Default is 64 parallel workers.
For example:

```python
parallel_run(dataset=dataset, model_producer=model_producer, metric_producer=metric_producer)
```

Generally, the higher the parrallelism, the faster run finishes. However, you may experience throttling or rejections from
cloud LLM provider. Also, a very large number of workers may strain the computer running it. Be careful and know what you are doing.

Another common pitfall is that errors from parallel workers may be less clear as trace stack and the original exception are not preserved (as they may not be serializable). To troubleshoot one may want temporarily convert script to using `run` instead. Then switch back to the `parallel_run`
after problem is addressed.

