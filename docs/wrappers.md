# Model Wrappers

Model wrappers are utility classes that wrap other models to modify their behavior. They can be composed together to create complex model pipelines.

## IgnoreSystemModel

Wraps a model and removes system message (if any) from the input. Useful when dataset contains system messages, but
model does not expect system.

```python
from redlite.model.hf_model import HFModel
from redlite.model import IgnoreSystemModel

model = IgnoreSystemModel(HFModel("mistralai/Mistral-Instruct-v0.2"))
```

## MakeSystemModel

Wraps a model and adds (or replaces) system message. Useful when dataset does not contains system messages, but
you want to provide one.

```python
from redlite.model.hf_model import HFModel
from redlite.model import MakeSystemModel

model = MakeSystemModel(HFModel("nvidia/NVIDIA-Nemotron-Nano-9B-v2"), system_prompt="/think")
```

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

## ThrottleModel

A model that wraps another model and throttles it calls to the specified rate.

```python
from redlite.model import CannedModel

model = ThrottleModel(OpenAIModel(), 5)
```

## ModerationModel

Wraps a model and filters conversation content using OpenAI's Moderation API. Before delegating to the inner model, all message contents are checked for potentially harmful content. If any content is flagged, the model returns a refusal message instead of processing the request.

This helps avoid having your OpenAI account flagged for Usage Policy Violations. See [OpenAI Safety Best Practices](https://platform.openai.com/docs/guides/safety-best-practices#use-our-free-moderation-api).

Requires an OpenAI API key (via `api_key` parameter or `OPENAI_API_KEY` environment variable).

For detail API and parameters, see [Reference](../../reference/redlite/model/#moderationmodel).

Example:

```python
from redlite.model.openai_model import OpenAIModel
from redlite.model import ModerationModel

# Create base model
base_model = OpenAIModel(model="gpt-4")

# Wrap with moderation
safe_model = ModerationModel(base_model)

# Safe content passes through to the base model
response = safe_model([{"role": "user", "content": "What is Python?"}])

# Harmful content is blocked and returns refusal message
response = safe_model([{"role": "user", "content": "harmful request"}])
# Returns: "I refuse to answer this question."
```

To filter out weapons-related questions, do this:

```python
from redlite.model import ModerationModel

base_model = ...  # your base model, i.e. OpenAIModel

safe_model = ModerationModel(base_model, threshold={"illicit/violent": 0.8})
```
