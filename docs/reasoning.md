# Reasoning models

Some models employ "reasoning" (a.k.a. "thinking") to produce better answers. The text of their "thinking" process pollutes
model output and makes it hard or impossible to compare with non-thinking models. It may be necessary to remove the "thinking trace"
from the output of these models.

## RemoveThinking wrapper

We provide [`RemoveThinking`](../../reference/redlite/model/#removethinking) model wrapper to deal with this.
This wrapper takes the underlying model output and strips off any thinking traces found.

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

In this example, `base_model` produces response that includes thinking trace, like this:

```text
<thinking>I am thinking and thinking... and thinking...</thinking>Here is my final answer
```

By wrapping `base_model` with `RemoveThinking`, the `model` will only produce `"Here is my final answer"`.

## Special tokens

Some models use special tokens to indicate thinking text block.
Specifically, models utilizing [OpenAI Harmony Standard](https://cookbook.openai.com/articles/openai-harmony)
use special tokens like `<|analysis|>`, `<|final|>`, etc.
You need to make sure that implementation does not strip these special tokens off.

For models deployed on [HuggingFace](https://hf.com) one may need to pass `skip_special_tokens=False`, otherwise
model tokenizer will internally remove the delimiting tokens (but not thinking text), and wrapper will not
be able to recognize and remove the thinking block.

Example:

```python
from redlite.model.hf_model import HFModel
from redlite.model import RemoveThinking


base_model = HFModel("openai/gpt-oss-20b", token=os.environ["HF_TOKEN"], skip_special_tokens=False);

model = RemoveThinking(base_model)
```