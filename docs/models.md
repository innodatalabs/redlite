# Built-in Models

## HuggingFace hub

Out-of the box we support models hosted on HuggingFace hub and using
[transformers](https://hf.co/transformers) framework backed by
[PyTorch](https://pytorch.org).

```python
from redlite.hf.hf_model import HFModel

model = HFModel(...)
```

## OpenAI Conversational Models

```python
from redlite.openai import OpenAIModel

model = OpenAIModel(...)
```

## Custom models

Custom models can be easily integrated, see the [Customization Guide](custom.md).
