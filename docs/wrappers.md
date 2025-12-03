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

## ParrotModel

A model that parrots back the last user message. Useful to establish performance baselines.

```python
from redlite.model import ParrotModel

model = ParrotModel()

assert model([{"role": "user", "content": "Hello"}]) == "Hello"
```

## CannedModel

A model that returns the same (canned) response regardless of user input. Useful to establish performance baselines.

```python
from redlite.model import CannedModel

model = CannedModel("Bye")

assert model([{"role": "user", "content": "Hello"}]) == "Bye"
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

Parameters:
- `model` - The model to wrap (any NamedModel)
- `api_key` - OpenAI API key (optional, uses OPENAI_API_KEY env var if not provided)
- `moderation_model` - Which moderation model to use (default: "omni-moderation-latest")
- `refusal_message` - Custom message to return when content is flagged (default: "I refuse to answer this question.")

Note: If the moderation API fails (network error, rate limit, etc.), the wrapper will fail closed (return refusal) to maintain safety guarantees.
