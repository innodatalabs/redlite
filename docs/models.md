# Built-in Models

## HuggingFace hub

Out-of the box we support models implemented with the [transformers](https://hf.co/transformers) framework
and hosted on [HuggingFace model hub](https://hf.co/models).

We presently only support models that use [PyTorch](https://pytorch.org) backend.
Support for other backends is on the roadmap.

Here is how to work with HuggingFace models:

```python
from redlite.model.hf_model import HFModel

model = HFModel(...)
```

Please see [Reference](../../reference/redlite/model/hf_model) documentation for more detail and availabel parameters.

## OpenAI Conversational Models

OpenAI conversational models (such as `gpt-3.5` or `gpt-4`) are available. Note that one needs a valid
OpenAI api key to do the prediction with these models.

Here is how to use OpenAI models:

```python
from redlite.openai import OpenAIModel

model = OpenAIModel(...)
```

Please see [Reference](../../reference/redlite/model/openai_model/) documentation for more detail and available parameters.

## IgnoreSystemModel

Wraps a model and removes system message (if any) from the input. Useful when dataset contains system messages, but
model does not expect system.

```python
from redlite.model.hf_model import HFModel
from redlite.model import IgnoreSystemModel

model = IgnoreSystemModel(HFModel("mistralai/Mistral-Instruct-v0.2"))
```

Please see [Reference](../../reference/redlite/model/) documentation for more detail.

## Custom models

Custom models can be easily integrated, see the [Customization Guide](custom.md).
