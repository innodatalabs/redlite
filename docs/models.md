# Built-in Models

## HuggingFace hub

Out-of the box we support models implemented with the [transformers](https://hf.co/transformers) framework
and hosted on [HuggingFace model hub](https://hf.co/models).

Here is how to work with HuggingFace models:

```python
from redlite.model.hf_model import HFModel

model = HFModel('mistralai/Mistral-7B-Instruct-v0.2', device_map='auto')
```

Please see [Reference](../../reference/redlite/model/hf_model) documentation for more detail and available parameters.

## OpenAI Conversational Models

OpenAI conversational models (such as `gpt-3.5` or `gpt-4`) are available. Note that one needs a valid
OpenAI api key to do the prediction with these models.

Here is how to use OpenAI models:

```python
from redlite.model.openai_model import OpenAIModel

model = OpenAIModel(...)
```

Please see [Reference](../../reference/redlite/model/openai_model/) documentation for more detail and available parameters.

## Anthropic Chat Models

Anthropic conversational models (e.g. Claude) are available. Note that one needs a valid
Anthropic api key to do the prediction with these models.

Here is how to use Anthropic models:

```python
from redlite.model.anthropic_model import AnthropicModel

model = AnthropicModel(...)
```

Please see [Reference](../../reference/redlite/model/anthropic_model/) documentation for more detail and available parameters.

## AWS Bedrock Text Generation Models

Use `AwsBedrockModel` to access models hosted on AWS Bedrock. Note that one needs a valid AWS key pair.

Here is how to use AWS Bedrock models:

```python
from redlite.model.aws_bedrock_model import AwsBedrockModel

model = AwsBedrockModel(...)
```

Please see [Reference](../../reference/redlite/model/aws_bedrock_model/) documentation for more detail and available parameters.

## IgnoreSystemModel

Wraps a model and removes system message (if any) from the input. Useful when dataset contains system messages, but
model does not expect system.

```python
from redlite.model.hf_model import HFModel
from redlite.model import IgnoreSystemModel

model = IgnoreSystemModel(HFModel("mistralai/Mistral-Instruct-v0.2"))
```

Please see [Reference](../../reference/redlite/model/) documentation for more detail.

## ConvertSystemToUserModel

Wraps a model and converts system message (if present) to the user one.
Useful when dataset contains system messages, but model does not expect system.

```python
from redlite.model.hf_model import HFModel
from redlite.model import ConvertSystemToUserModel

model = ConvertSystemToUSerModel(
    HFModel("mistralai/Mistral-Instruct-v0.2"),
    assistant_confirmation="Sure thing!"
)
```

Please see [Reference](../../reference/redlite/model/) documentation for more detail.

## ParrotModel

A model that parrots back the last user message. Useful to establish performance baselines.

```python
from redlite.model import ParrotModel

model = ParrotModel()

assert model([{"role": "user", "content": "Hello"}]) == "Hello"
```

Please see [Reference](../../reference/redlite/model/) documentation for more detail.

## CannedModel

A model that returns the same (canned) response regardless of user input. Useful to establish performance baselines.

```python
from redlite.model import CannedModel

model = CannedModel("Bye")

assert model([{"role": "user", "content": "Hello"}]) == "Bye"
```

Please see [Reference](../../reference/redlite/model/) documentation for more detail.

## Custom models

Custom models can be easily integrated, see the [Customization Guide](custom.md).
