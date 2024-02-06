# Built-in Models

## HuggingFace hub

Out-of the box we support models implemented with the [transformers](https://hf.co/transformers) framework
and hosted on [HuggingFace model hub](https://hf.co/models).

We presently only support models that use [PyTorch](https://pytorch.org) backend.
Support for other backends is on the roadmap.

Here is how to work with HuggingFace models:

```python
from redlite.hf.hf_model import HFModel

model = HFModel(...)
```

Please see [Reference](../reference) documentation for more detail and availabel parameters.

## OpenAI Conversational Models

OpenAI conversational models (such as `gpt-3.5` or `gpt-4`) are available. Note that one needs a valid
OpenAI api key to do the prediction with these models.

Here is how to use OpenAI models:

```python
from redlite.openai import OpenAIModel

model = OpenAIModel(...)
```

Please see [Reference](../reference) documentation for more detail and available parameters.

## Custom models

Custom models can be easily integrated, see the [Customization Guide](custom.md).
