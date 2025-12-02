# Reasoning models

## RemoveThinking wrapper

Some models employ "reasoning" (a.k.a. "thinking) to produce better answers. The text of their "thinking" process pollutes
model output and makes it hard or impossible to compare with non-thinking models. It is desirable to remove the "thinking trace"
from the output of these models.

We provide [`RemoveThinking`](../../reference/redlite/model/#removethinking) model wrapper to deal with this. This wrapper takes the underlying model output
and strips off any thinking traces.

Example:

```python
from redlite.model.openai_model import OpenAIModel
from redlite.model import RemoveThinking

base_model = OpenAIModel(
    model= "nvidia/llama-3.3-nemotron-super-49b-v1.5",
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.environ["NVIDIA_API_KEY"],
)

model = RemoveThinking(base_model)
```

## Special tokens

Some models use special tokens to indicate thinking text block. You need to set `strip_special_tokens=False` in the model
parameters. Otherwise model tokenizer will internally remove delimiting tokens (but not thinking text), and wrapper will not
be able to recognize the thinking block.

Example:

```python
from redlite.model.hf_model import HFModel
from redlite.model import RemoveThinking


base_model = HFModel("openai/gpt-oss-20b", token=os.environ["HF_TOKEN"], strip_special_tokens=False);

model = RemoveThinking(base_model)
