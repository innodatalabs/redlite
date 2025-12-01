import re
from .._core import NamedModel, Message, MissingDependencyError
from .._util import sha_digest

try:
    from transformers import pipeline
except ImportError as err:
    raise MissingDependencyError("Please install transformers library") from err


class HFModel(NamedModel):
    """
    Model loaded from HuggingFace hub.

    - **hf_name** (`str`): name of the model on HuggingFace hub.
    - **task** (`str`): Pipeline task. Default is `text-generation`. If using multimodal models,
            you may need to change it to `image-text-to-text`. Refer to model documentation on HuggingFace.
    - **remove_thinking_trace** (`bool`): when set to `True`, will attempt to remove
            any "thinking trace" added by some models (e.g., OpenAI OSS models). Default is `False`.
    - **pipeline_params** (`dict[str,Any]`): Other pipeline params, will be passed as-is to the
            HF pipeline constructor.
    """

    def __init__(
        self,
        hf_name: str,
        task="text-generation",
        remove_thinking_trace=False,
        **pipeline_params,
    ):
        args = {
            "model": hf_name,
            "use_fast": False,
            **pipeline_params,
        }  # allow overwriting "model" (hacky) -MK; allow overwriting "use_fast"
        if remove_thinking_trace:
            args['skip_special_tokens'] = False
        self.__pipeline = pipeline(task=task, **args)
        self.__remove_thinking_trace = remove_thinking_trace

        name = "hf:" + hf_name
        if len(pipeline_params) > 0 or remove_thinking_trace:
            obj = {x: str(pipeline_params[x]) for x in pipeline_params}
            if remove_thinking_trace:
                obj['remove_thinking_trace'] = 'True'
            name += "@" + sha_digest(obj)[:6]

        super().__init__(name, self.__predict)
        print(f"HFModel {hf_name} placed on device {self.__pipeline.device}")

    def __predict(self, messages: list[Message]) -> str:
        pad_token_id = self.__pipeline.generation_config.pad_token_id
        if pad_token_id is None:
            pad_token_id = self.__pipeline.generation_config.eos_token_id
        if self.__pipeline.task == "image-text-to-text":
            # may need to massage incoming message format
            conversation = [_convert_for_image_text_to_text(x) for x in messages]
        else:
            # deep copy messages as pipeline may mess with them
            conversation = [dict(x) for x in messages]
        out = self.__pipeline(conversation, pad_token_id=pad_token_id)
        assert out[0]["generated_text"][-1]["role"] == "assistant", out
        content = out[0]["generated_text"][-1]["content"]
        if self.__remove_thinking_trace:
            content = _remove_thinking_trace(content)
            content = content.split("\n")[0]
        return content


def _convert_for_image_text_to_text(message):
    out = {**message}
    if type(message["content"]) is str:
        out["content"] = [{"type": "text", "text": message["content"]}]
    return out


_RE_THINKING_TRACE = {
    'openai-oss': r'<\|start\|>assistant<\|channel\|>final<\|message\|>(.*)<\|return\|>$',
}

def _remove_thinking_trace(content: str) -> str:
    for pattern in _RE_THINKING_TRACE.values():
        mtc = re.search(pattern, content, flags=re.DOTALL | re.IGNORECASE)
        if mtc is not None:
            return mtc.group(1).strip()
    print("Warning: could not remove thinking trace from content")
    return content